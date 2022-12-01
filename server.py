from flask import Flask, request, abort
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)
# This model was chosen because it is extremely small, not because it is
# especially accurate. For a more accurate model, use something like
# "distilbert-base-uncased-finetuned-sst-2-english"
model = "philschmid/tiny-bert-sst2-distilled"

tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForSequenceClassification.from_pretrained(model)


@app.route("/sentiment", methods=["POST"])
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
