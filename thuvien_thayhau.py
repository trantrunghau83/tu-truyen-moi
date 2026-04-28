import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN "SIÊU RÕ NÉT" - CHỮ ĐEN NỀN TRẮNG TUYỆT ĐỐI
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    /* 1. ÉP NỀN TRẮNG TOÀN BỘ TRANG */
    .stApp, .stAppViewMain, .main {
        background-color: #FFFFFF !important;
    }
    
    /* 2. ÉP CHỮ ĐEN CHO TẤT CẢ CÁC THÀNH PHẦN (Tiêu đề, đoạn văn, nhãn, v.v.) */
    h1, h2, h3, h4, h5, h6, p, span, label, li, div, small {
        color: #000000 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* 3. KHUNG NỘI DUNG SÁCH (Rõ ràng như giấy in) */
    .book-content-box {
        background-color: #F9FAFB !important; /* Xám cực nhẹ để phân biệt vùng đọc */
        padding: 30px !important;
        border-radius: 12px !important;
        border: 1px solid #E5E7EB !important;
        color: #000000 !important;
        line-height: 1.8 !important;
        font-size: 19px !important;
        margin-top: 20px !important;
    }

    /* 4. TÙY CHỈNH NÚT BẤM (Nền màu xanh đậm, chữ màu trắng để nổi bật) */
    .stButton>button {
        background-color: #1E40AF !important;
        border: none !important;
        border-radius: 8px !important;
        width: 100% !important;
        height: 50px !important;
    }
    
    /* Chữ TRONG nút bấm phải là màu trắng */
    .stButton>button p, .stButton>button span, .stButton>button div {
        color: #FFFFFF !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }

    /* 5. KHUNG BÌNH LUẬN (Mạng xã hội) */
    .comment-card {
        background-color: #F3F4F6 !important;
        padding: 15px !important;
        border-radius: 10px !important;
        margin-bottom: 15px !important;
        border-left: 5px solid #1E40AF !important;
    }
    
    /* 6. FIX Ô NHẬP LIỆU */
    input, textarea, [data-baseweb="base-input"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #D1D5DB !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. NỘI DUNG SÁCH
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """
        Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ. Và có những người thầy, mỗi ngày lặng lẽ đến trường, mang theo tri thức, tình thương và trách nhiệm để vun trồng tương lai cho đất nước. <br><br>
        Cuốn sách này kể về thầy Trần Trung Hậu – một giáo viên môn Tin học tại Trường THCS Thuận Hưng, Thành phố Cần Thơ...
        """,
        "Chương 1: Tuổi thơ": "Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ...",
        "Chương 2: Bước chân vào nghề": "Năm 2000, thầy Trần Trung Hậu chính thức bước vào nghề giáo...",
        "Chương 3: Người thầy thời đại số": "Nhiều người nghĩ dạy Tin học là dạy thao tác trên máy tính...",
        "Chương 5: Câu chuyện học trò": "Trong hành trình dạy học, có những niềm vui lớn, nhưng cũng có những nỗi buồn...",
        "Kết luận": "Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. HIỂN THỊ GIAO DIỆN
st.markdown("<h1 style='text-align: center;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)

# Mục lục bên trái
st.sidebar.markdown("### 📖 MỤC LỤC")
chon_chuong = st.sidebar.radio("Chọn chương:", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Nội dung chính
st.markdown(f"## {chon_chuong}")
noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]

# Ép nội dung vào khung với màu chữ đen chuẩn
st.markdown(f"<div class='book-content-box'>{noidung}</div>", unsafe_allow_html=True)

st.markdown("---")

# 4. PHẦN BÌNH LUẬN (MẠNG XÃ HỘI)
st.subheader("💬 Cảm nhận từ bạn đọc")

with st.form("comment_form", clear_on_submit=True):
    ten = st.text_input("Tên của bạn:")
    noidung_bl = st.text_area("Lời nhắn gửi:")
    gui = st.form_submit_button("GỬI BÌNH LUẬN")
    
    if gui and ten and noidung_bl:
        st.session_state.comments.insert(0, {
            "name": ten, 
            "text": noidung_bl, 
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        st.rerun()

# Hiển thị các bình luận
for c in st.session_state.comments:
    st.markdown(f"""
    <div class='comment-card'>
        <strong>👤 {c['name']}</strong> <small style='color: #6B7280;'>({c['time']})</small><br>
        <p style='margin-top:8px;'>{c['text']}</p>
    </div>
    """, unsafe_allow_html=True)
