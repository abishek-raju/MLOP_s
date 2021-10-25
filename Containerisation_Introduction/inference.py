# https://github.com/Cadene/pretrained-models.pytorch
# import pretrainedmodels
import torch
# import pretrainedmodels.utils as utils
import pickle
import urllib.request as urllib2
# print(pretrainedmodels.pretrained_settings['resnet18'])


def classify_image(path_img,top_predictions_to_output = 1):
    model_name = 'resnet18'
    model = pretrainedmodels.__dict__[model_name]()
    model.eval()
    load_img = utils.LoadImage()
    tf_img = utils.TransformImage(model) 
    input_img = load_img(path_img)
    input_tensor = tf_img(input_img)         # 3x400x225 -> 3x299x299 size may differ
    input_tensor = input_tensor.unsqueeze(0) # 3x299x299 -> 1x3x299x299
    input = torch.autograd.Variable(input_tensor,
        requires_grad=False)
    output_logits = model(input)
    output_probs = output_logits.softmax(1)
    conf,label_id = output_probs.topk(top_predictions_to_output)
    imagenet_class_dict = pickle.load(urllib2.urlopen('https://gist.githubusercontent.com/yrevar/6135f1bd8dcf2e0cc683/raw/d133d61a09d7e5a3b36b8c111a8dd5c4b5d560ee/imagenet1000_clsid_to_human.pkl'))
    return conf.tolist()[0],[imagenet_class_dict[l_id] for l_id in label_id.tolist()[0]]


# print(classify_image("/home/rampfire/Downloads/german_shepard.jpeg"))