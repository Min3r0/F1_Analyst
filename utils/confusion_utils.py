import io
import base64
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

def get_confusion_image(y_true, y_pred, model_name):
    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay.from_predictions(
        y_true, y_pred, display_labels=["Faux", "Vrai"],
        cmap="Blues", ax=ax
    )
    ax.set_title(f"Matrice de confusion : {model_name}")
    ax.set_xlabel("Prédit")
    ax.set_ylabel("Réel")
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{encoded}"
