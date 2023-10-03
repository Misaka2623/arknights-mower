import os


ocr = None


def initialize_ocr():
    det_model_dir = os.path.join(os.getcwd(), "tmp", "paddle", "det", "ch")
    rec_model_dir = os.path.join(os.getcwd(), "tmp", "paddle", "rec", "ch")
    cls_model_dir = os.path.join(os.getcwd(), "tmp", "paddle", "cls")

    global ocr
    if not ocr:
        from paddleocr import PaddleOCR

        ocr = PaddleOCR(
            enable_mkldnn=False,
            use_angle_cls=False,
            cls=False,
            show_log=False,
            det_model_dir=det_model_dir,
            rec_model_dir=rec_model_dir,
            cls_model_dir=cls_model_dir,
        )