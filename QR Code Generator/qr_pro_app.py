import sys
import qrcode
from PIL import Image
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QFileDialog, QColorDialog,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFrame
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt


class QRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.resize(900, 520)

        self.qr_color = "#000000"
        self.logo_path = None
        self.dark_mode = False

        self.init_ui()
        self.apply_light_theme()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # ======= CONTENT AREA =======
        content_layout = QHBoxLayout()

        # ---------- LEFT PANEL ----------
        left_panel = QFrame()
        left_panel.setFixedWidth(400)
        left_layout = QVBoxLayout()

        # Logo TanLoc (nằm bên trái panel)
        self.brand_logo = QLabel()
        pix = QPixmap("tanloc_logo.png")
        self.brand_logo.setPixmap(
            pix.scaled(120, 60, Qt.AspectRatioMode.KeepAspectRatio)
        )
        self.brand_logo.setAlignment(Qt.AlignmentFlag.AlignLeft)

        left_layout.addWidget(self.brand_logo)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Nhập nội dung hoặc URL...")
        left_layout.addWidget(self.input)

        grid = QGridLayout()

        self.btn_color = QPushButton("Chọn màu")
        self.btn_logo = QPushButton("Chọn logo QR")
        self.btn_generate = QPushButton("Tạo QR")
        self.btn_save = QPushButton("Lưu QR")
        self.btn_theme = QPushButton("Chuyển Dark / Light")

        grid.addWidget(self.btn_color, 0, 0)
        grid.addWidget(self.btn_logo, 0, 1)
        grid.addWidget(self.btn_generate, 1, 0)
        grid.addWidget(self.btn_save, 1, 1)
        grid.addWidget(self.btn_theme, 2, 0, 1, 2)

        left_layout.addLayout(grid)
        left_layout.addStretch()

        left_panel.setLayout(left_layout)

        # ---------- RIGHT PANEL ----------
        right_panel = QFrame()
        right_layout = QVBoxLayout()

        self.preview = QLabel("QR Preview")
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview.setMinimumSize(400, 400)

        right_layout.addWidget(self.preview)
        right_panel.setLayout(right_layout)

        content_layout.addWidget(left_panel)
        content_layout.addWidget(right_panel)

        # ======= FOOTER =======
        footer = QLabel("QR Code Generator By ShikoFT © 2026")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setStyleSheet("font-size: 10px; opacity: 0.6;")

        # ======= ADD TO MAIN =======
        main_layout.addLayout(content_layout)
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

        # ======= CONNECT =======
        self.btn_color.clicked.connect(self.choose_color)
        self.btn_logo.clicked.connect(self.choose_logo)
        self.btn_generate.clicked.connect(self.generate_qr)
        self.btn_save.clicked.connect(self.save_qr)
        self.btn_theme.clicked.connect(self.toggle_theme)

    # ================= FUNCTIONS =================

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.qr_color = color.name()

    def choose_logo(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Chọn logo", "", "Images (*.png *.jpg *.jpeg)"
        )
        if path:
            self.logo_path = path

    def generate_qr(self):
        data = self.input.text()
        if not data:
            return

        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color=self.qr_color,
            back_color="white"
        ).convert("RGBA")

        if self.logo_path:
            logo = Image.open(self.logo_path)
            qr_w, qr_h = img.size
            logo_size = qr_w // 4
            logo = logo.resize((logo_size, logo_size))
            pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
            img.paste(logo, pos, logo if logo.mode == "RGBA" else None)

        img.save("temp_qr.png")

        pixmap = QPixmap("temp_qr.png")
        self.preview.setPixmap(
            pixmap.scaled(
                350, 350,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

    def save_qr(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Lưu QR", "", "PNG Files (*.png)"
        )
        if path:
            Image.open("temp_qr.png").save(path)

    # ================= THEME =================

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #f5f5f5; color: #222; }
            QLineEdit, QPushButton {
                background-color: white;
                border: 1px solid #ccc;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #e6e6e6;
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: #ddd; }
            QLineEdit, QPushButton {
                background-color: #2d2d2d;
                border: 1px solid #555;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #3c3c3c;
            }
        """)

    def toggle_theme(self):
        if self.dark_mode:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()

        self.dark_mode = not self.dark_mode


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRApp()
    window.show()
    sys.exit(app.exec())
