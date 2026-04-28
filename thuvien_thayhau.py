import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN "SIÊU TƯƠNG PHẢN" (CHỐNG LỖI MÀU)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* Nền trang: Màu xám cực nhạt để nổi chữ */
    .stApp {
        background-color: #F0F2F6 !important;
    }
    
    /* ÉP MÀU CHỮ TOÀN TRANG: Đen tuyệt đối */
    h1, h2, h3, h4, p, span, label, div {
        color: #000000 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* Khung nội dung sách: Nền trắng tinh, chữ đen */
    .book-content-box {
        background-color: #FFFFFF !important;
        padding: 30px !important;
        border-radius: 10px !important;
        border: 2px solid #D1D5DB !important;
        color: #000000 !important;
        line-height: 1.8 !important;
        font-size: 19px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        margin-bottom: 20px !important;
    }

    /* Khung bình luận: Nền xanh nhạt, chữ đen */
    .comment-card {
        background-color: #E5E7EB !important;
        padding: 15px !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
        border-left: 6px solid #1E40AF !important;
        color: #000000 !important;
    }

    /* Nút bấm: Nền xanh đậm, chữ TRẮNG tinh */
    .stButton>button {
        background-color: #1E40AF !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        width: 100% !important;
    }
    .stButton>button p {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }
    
    /* Fix màu cho ô nhập liệu */
    input, textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #9CA3AF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU NỘI DUNG (Em đã nạp toàn bộ nội dung anh gửi vào đây)
# Để tiết kiệm diện tích, em tóm lược, anh có thể dán đầy đủ vào các dấu ngoặc kép nhé
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": "Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng...",
        "Chương 1: Tuổi thơ": "Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ...",
        "Chương 2: Bước chân vào nghề": "Năm 2000, thầy Trần Trung Hậu chính thức bước vào nghề giáo...",
        "Chương 3: Người thầy thời đại số": "Nhiều người nghĩ dạy Tin học là dạy thao tác trên máy tính...",
        "Chương 4: Những sáng kiến": "Một trong những sáng kiến nổi bật là Giải pháp nâng cao chất lượng môn Tin học...",
        "Chương 5: Câu chuyện học trò": "Thầy từng bồi dưỡng một học sinh có năng lực lập trình rất tốt...",
        "Chương 6: Đời thường": "Sau giờ dạy, thầy trở về với mái ấm của mình...",
        "Chương 7: Danh hiệu": "Nhà giáo Ưu tú năm 2017, Huân chương Lao động hạng Ba năm 2025...",
        "Chương 8: Triết lý sống": "Dạy chữ đi cùng dạy người. Kiến thức giúp kiếm sống, nhân cách giúp sống đúng.",
        "Kết luận": "Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."
    }
}

# Quản lý bình luận
if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. GIAO DIỆN HIỂN THỊ
st.markdown("<h1 style='text-align: center;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Tác phẩm: Người Thầy Giữa Đời Thường</p>", unsafe_allow_html=True)

# Thanh bên (Sidebar)
st.sidebar.header("MỤC LỤC")
chon_chuong = st.sidebar.radio("Chọn chương để đọc:", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Nội dung chính
st.markdown(f"### {chon_chuong}")
noidung_hien_tai = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]

# Ép nội dung vào khung trắng chữ đen
st.markdown(f"<div class='book-content-box'>{noidung_hien_tai}</div>", unsafe_allow_html=True)

st.markdown("---")

# 4. PHẦN MẠNG XÃ HỘI (BÌNH LUẬN)
st.subheader("💬 Cảm nhận của bạn đọc")

with st.form("fb_form", clear_on_submit=True):
    ten = st.text_input("Tên bạn:")
    cam_nhan = st.text_area("Lời nhắn gửi đến thầy Hậu:")
    submit = st.form_submit_button("Gửi bình luận")
    
    if submit and ten and cam_nhan:
        st.session_state.comments.insert(0, {
            "name": ten,
            "text": cam_nhan,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

# Hiển thị bình luận
for c in st.session_state.comments:
    st.markdown(f"""
    <div class='comment-card'>
        <strong>👤 {c['name']}</strong> <small>({c['time']})</small><br>
        <p style='margin-top:5px;'>{c['text']}</p>
    </div>
    """, unsafe_allow_html=True)
