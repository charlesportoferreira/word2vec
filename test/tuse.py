import tensorflow_hub as hub
import tensorflow as tf

tf.logging.set_verbosity(0)


def embedUSE(module):
    with tf.Graph().as_default():
        sentences = tf.placeholder(tf.string)
        embed = hub.Module(module)
        embeddings = embed(sentences)
        session = tf.train.MonitoredSession()
    return lambda x: session.run(embeddings, {sentences: x})


# Applies USE to any token provided (w,s,p)
# returns a tensor (X, 512) where X : number of tkoens passed -as list - 512 dimensions

module1 = "https://tfhub.dev/google/universal-sentence-encoder-large/3"  # newer module
module2 = "https://tfhub.dev/google/universal-sentence-encoder-large/2"  # older module

applyUSE = embedUSE(module1)

x = [
    "The quick brown fox jumps over the lazy dog.",
    "I am a sentence for which I would like to get its embedding",
]

x2 = ['terry', 'eats', 'ice', 'cream']

vec = applyUSE(x2)
print(vec.shape)
print(vec)

c = applyUSE(['3243442443324324rdfdsfdsfdsfsdfdsfdsfdsfsfdsfdfdsf sdfdsfdsf sdfdsfdfreewr'])

print('c', c)

'''
print(f2(x))
print(f2_dup(x))
# Returns zeros showing the module is stable across instantiations.
print(np.linalg.norm(f2(x) - f2_dup(x)))

# ISSUE: returns 0.3 showing the embeddings per example depend on other elements in the batch.
print(np.linalg.norm(f2(x[0:1]) - f2(x)[0:1]))

'''
