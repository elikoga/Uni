CHARS = ["a", "b"]


def tokenize(s):
    return [CHARS.index(c) for c in s]


def untok(tok):
    return CHARS[tok]


# examples:
tokenize("aabaa")  # => [0, 0, 1, 0, 0]
untok(0)  # => "a"
untok(1)  # => "b"

import numpy as np


def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def linear(x, W, b):
    return x @ W + b


def attention(Q, K, V, mask):
    # print q, k, v, mask shapes
    print(Q.shape, K.shape, V.shape, mask.shape)
    return softmax(Q @ K.T / np.sqrt(Q.shape[-1]) + mask) @ V


def causal_self_attention(x, c_attn, c_proj):
    x = linear(x, **c_attn)

    q, k, v = np.split(x, 3, axis=-1)

    mask = (1 - np.tri(x.shape[0], dtype=x.dtype)) * -1e10

    x = attention(q, k, v, mask)

    return linear(x, **c_proj)


def transformer_block(x, **attn):
    x = x + causal_self_attention(x, **attn)
    return x


def transformer(inputs, wte, wpe, blocks):
    x = wte[inputs] + wpe[range(len(inputs))]
    for block in blocks:
        x = transformer_block(x, **block)
    return x @ wte.T


N_CTX = 5
N_VOCAB = 2
N_EMB = 8

Lg = 1024  # large

MODEL = {
    # "wte": np.random.randn(N_VOCAB, N_EMB),
    "wte": np.array([[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]]),
    # "wpe": np.random.randn(N_CTX, N_EMB),
    "wpe": np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
        ]
    ),
    "blocks": [
        {
            "c_attn": {
                "b": np.zeros(N_EMB * 3),
                "W": np.array(
                    # this is where the magic happens
                    # fmt: off
                        [
                          [Lg, 0., 0., 0., 0., 0., 0., 0.,  # q
                            1., 0., 0., 0., 0., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., 0.], # v
                          [Lg, Lg, 0., 0., 0., 0., 0., 0.,  # q
                            0., 1., 0., 0., 0., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., 0.], # v
                          [0., Lg, Lg, 0., 0., 0., 0., 0.,  # q
                            0., 0., 1., 0., 0., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., 0.], # v
                          [0., 0., Lg, Lg, 0., 0., 0., 0.,  # q
                            0., 0., 0., 1., 0., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., 0.], # v
                          [0., 0., 0., Lg, Lg, 0., 0., 0.,  # q
                            0., 0., 0., 0., 1., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., 0.], # v
                          [0., 0., 0., 0., 0., 0., 0., 0.,  # q
                            0., 0., 0., 0., 0., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., 1.], # v
                          [0., 0., 0., 0., 0., 0., 0., 0.,  # q
                            0., 0., 0., 0., 0., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., -1], # v
                          [0., 0., 0., 0., 0., 0., 0., 0.,  # q
                            0., 0., 0., 0., 0., 0., 0., 0.,  # k
                              0., 0., 0., 0., 0., 0., 0., 0.], # v
                        ]
                    # fmt: on
                ),
            },
            "c_proj": {  # weights to project attn result back to embedding space
                "b": [0, 0, 0, 0, 0, Lg, 0, 0],
                "W": np.array(
                    [
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, -Lg, Lg, 0],
                    ]
                ),
            },
        },
    ],
}


def predict(s):
    tokens = tokenize(s)[-5:]
    logits = transformer(tokens, **MODEL)
    probs = softmax(logits)

    for i, tok in enumerate(tokens):
        pred = np.argmax(probs[i])
        print(
            f"{untok(tok)} ({tok}): next={untok(pred)} ({pred}) probs={probs[i]} logits={logits[i]}"
        )

    return np.argmax(probs[-1])


def complete(s, max_new_tokens=10):
    tokens = tokenize(s)
    while len(tokens) < len(s) + max_new_tokens:
        logits = transformer(tokens[-N_CTX:], **MODEL)
        probs = softmax(logits)
        pred = np.argmax(probs[-1])
        tokens.append(pred)
    return s + " :: " + "".join(untok(t) for t in tokens[len(s) :])


print(complete("a"))  # a :: baabaabaab
print(complete("ba"))  # ba :: abaabaabaa
print(complete("abaab"))  # abaab :: aabaabaaba
