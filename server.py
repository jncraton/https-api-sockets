from flask import Flask, request, abort
import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("philschmid/tiny-bert-sst2-distilled")
model = AutoModelForSequenceClassification.from_pretrained("philschmid/tiny-bert-sst2-distilled")

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
