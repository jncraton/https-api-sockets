from flask import Flask, request, abort
import json
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

app = Flask(__name__)

tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)


@app.route("/", methods=["POST"])
def get_sentiment():
    if len(request.data) > 64:
        abort(413)
    inputs = tokenizer(request.data.decode("utf8"), return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    label = model.config.id2label[logits.argmax().item()]

    print(request.data.decode("utf8"), logits, label)
    return label.lower()


if __name__ == "__main__":
    app.run("0.0.0.0", port=1212, threaded=True)
