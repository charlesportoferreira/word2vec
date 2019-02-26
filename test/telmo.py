# Using ALLEN NLP
from allennlp.commands.elmo import ElmoEmbedder

# def embedElmo(model, tokens):
#    vectors = model.embed_sentence(tokens)
#    return vectors
#
#
## It returns a numpy/tensor with the following (x, y, z)
## x : three ANN layers - we want the top layer [2] (weighted sum), the other are internal layers
## x[a][b] : a - Layers, b - token position
## y : number of tokens-embedded
## z : dimensions
# elmo_model = ElmoEmbedder()  # model
# phrase = ["house", 'of', 'cards']
# w1 = ['house']
# w2 = ['of']
# w3 = ['cards']
# vectors = embedElmo(elmo_model, phrase)
# v1 = embedElmo(elmo_model, w1)
# v2 = embedElmo(elmo_model, w2)
# v3 = embedElmo(elmo_model, w3)
#
# print("----------------------")
# print('p1 : ', vectors[0][0])
# print('w1 : ', v1[0][0])
# print("----------------------")
#
# print("----------------------")
# print('p2 : ', vectors[0][1])
# print('w2 : ', v2[0][0])
# print("----------------------")
#
# print("----------------------")
# print('p3 : ', vectors[0][2])
# print('w3 : ', v3[0][0])
# print("----------------------")

# print('sent1 : ', vectors[0][0])  # top layer for word #0tmux a
# print('sent1 : ', vectors[1][0])  # top layer for word #0tmux a
# print('sent1 : ', vectors[2][0])  # top layer for word #0tmux a
# print('sent2 : ', vectors[2][1])  # top layer for word #0tmux a
#
# print('test: ', vectors[0][1])
# print('v1 : ', v1[2][0])  # top layer for word #0tmux a
# print('v2: ', v2[2][0])  # top layer for word #0tmux a
# print('v3 : ', v3[0][0])  # top layer for word #0tmux a
# print('v4: ', v4[0][0])  # top layer for word #0tmux a
#
#
# # Using TensorFlow
import tensorflow as tf
import tensorflow_hub as hub


#
#
# # we download model https://tfhub.dev/google/elmo/2?tf-hub-format=compressed
#
def embedElmo2(elmo_module):
    with tf.Graph().as_default():
        sentences = tf.placeholder(tf.string)
        embed = hub.Module(elmo_module)
        embeddings = embed(sentences)
        session = tf.train.MonitoredSession()
    return lambda x: session.run(embeddings, {sentences: x})


# Lambda function that initialize the model/tf to encode sentences
# returns a (X,1024) tensor (numpy), where x : is the weighted vector of ELMo for each token passed

embed_fn = embedElmo2('https://tfhub.dev/google/elmo/2')  # initialize module
v1 = embed_fn(["house"])
print("house:  ", v1)

embed_fn2 = embedElmo2('https://tfhub.dev/google/elmo/2')  # initialize module
v2 = embed_fn2(["house"])
print('house:  ', v2)

# a = embed_fn(["house", "of", "cards"])
# b = embed_fn(["house"])
# c = embed_fn(["of"])
# d = embed_fn(["cards"])
# print('shape:  ', a.shape)
# print('house:  ', a)
#
# print("-------------------------------------")
# print("house", a[0])
# print('house:  ', b)
# print("-------------------------------------")
# print("-------------------------------------")
# print("of", a[1])
# print('of:  ', c)
# print("-------------------------------------")
# print("-------------------------------------")
# print("cards", a[2])
# print('cards:  ', d)
# print("-------------------------------------")
#
# print("-------------------------------------")
# print('vector dimensions:  ', a.shape[1])
# print('number of vectors:  ', a.shape[0])
# print("-------------------------------------")


'''
#here we need to have the length size
module = "https://tfhub.dev/google/elmo/2" # it is possible to download too
elmo = hub.Module(module, trainable=True)
tokens_input = [["the", "cat"], ['ede',''], ['sssss','']]
tokens_length = [2,1,1]
embeddings = elmo(inputs={"tokens": tokens_input, "sequence_len": tokens_length}, signature="tokens", as_dict=True)["elmo"]

with tf.Session() as session:
    session.run([tf.global_variables_initializer(), tf.tables_initializer()])
    embs = (session.run(embeddings))
#[sentence index][word index]
# only returns the weighted average vector embeddigns
print(embs.shape)
print(embs[0][0])
print(embs[1][1])
'''

'''
elmo = ElmoEmbedder()
tokens = ["the", '', 'dd', 'sadsada', 'asddada']
# tokens = ["I"]
vectors = elmo.embed_sentence(tokens)

#layer #word
print('the 0 : ', vectors[0][0])
print('the 1 : ', vectors[1][0])
print('the 2 : ', vectors[2][0])

print(vectors.shape)
'''
