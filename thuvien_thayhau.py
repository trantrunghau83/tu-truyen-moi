import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH HỆ THỐNG - KHÓA CHẾ ĐỘ SÁNG (LIGHT MODE)
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="wide")

st.markdown("""
    <style>
    /* 1. ÉP NỀN TRẮNG TOÀN DIỆN */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* 2. ÉP TẤT CẢ CHỮ TRONG HỆ THỐNG THÀNH MÀU ĐEN ĐẬM */
    /* Bao gồm tiêu đề, đoạn văn, nhãn, các thành phần của Streamlit */
    h1, h2, h3, h4, p, span, label, div, .stMarkdown {
        color: #1A1A1A !important;
        font-family: 'Segoe UI', Arial, sans-serif !important;
    }

    /* 3. TẠO KHUNG ĐỌC SÁCH RÕ NÉT */
    .book-container {
        background-color: #F8F9FA !important; /* Nền xám cực nhẹ để nổi bật vùng đọc */
        padding: 30px !important;
        border-radius: 15px !important;
        border: 2px solid #EEEEEE !important;
        margin: 20px 0px !important;
    }

    /* 4. FIX MÀU CHO SIDEBAR (CỘT TRÁI) */
    section[data-testid="stSidebar"] {
        background-color: #F1F5F9 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #1A1A1A !important;
    }

    /* 5. NÚT BẤM (Màu xanh đậm, chữ trắng để tương phản) */
    .stButton>button {
        background-color: #1E40AF !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
    }
    
    /* Đảm bảo chữ trong nút luôn trắng */
    .stButton>button p {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU NỘI DUNG (Anh dán nội dung của anh vào đây)
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng. Có những cuộc đời không ồn ào nhưng để lại dấu ấn sâu sắc trong lòng bao thế hệ...""",
        "Chương 1: Tuổi thơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc – vùng đất hiền hòa của Thành phố Cần Thơ – cậu bé Trần Trung Hậu chào đời...""",
        "Kết luận": """Giữa đời thường, có những con người sống lặng lẽ mà lớn lao."""
    }
}

if 'comments' not in st.session_state:
    st.session_state.comments = []

# 3. HIỂN THỊ (DÙNG THẺ HTML TRỰC TIẾP ĐỂ ÉP MÀU ĐEN)

# Tiêu đề chính - Cột phải
st.markdown("<h1 style='text-align: center; color: #1E40AF !important;'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563 !important; font-style: italic;'>Nơi lưu giữ những ký ức và tri thức</p>", unsafe_allow_html=True)

# Mục lục - Cột trái
st.sidebar.markdown("<h2 style='color: #1E40AF !important;'>📖 CHỌN CHƯƠNG</h2>", unsafe_allow_html=True)
chon_chuong = st.sidebar.radio("", list(sach_du_lieu["Người Thầy Giữa Đời Thường"].keys()))

# Nội dung chính
st.markdown(f"<h2 style='color: #1A1A1A !important;'>📖 {chon_chuong}</h2>", unsafe_allow_html=True)

noidung = sach_du_lieu["Người Thầy Giữa Đời Thường"][chon_chuong]
st.markdown(f"""
    <div class='book-container'>
        <p style='color: #1A1A1A !important; font-size: 18px; line-height: 1.8;'>
            {noidung}
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #E5E7EB;'>", unsafe_allow_html=True)

# 4. PHẦN BÌNH LUẬN
st.markdown("<h3 style='color: #1E40AF !important;'>💬 Bạn đọc nhận xét</h3>", unsafe_allow_html=True)

with st.form("comment_box", clear_on_submit=True):
    # Tạo nhãn bằng HTML đen để không bị lỗi
    st.markdown("<p style='color: black !important; font-weight: bold;'>Tên của anh/chị:</p>", unsafe_allow_html=True)
    ten = st.text_input("", label_visibility="collapsed")
    
    st.markdown("<p style='color: black !important; font-weight: bold;'>Cảm nhận:</p>", unsafe_allow_html=True)
    bl = st.text_area("", label_visibility="collapsed")
    
    submit = st.form_submit_button("GỬI BÌNH LUẬN")
    
    if submit and ten and bl:
        st.session_state.comments.insert(0, {"name": ten, "text": bl, "time": datetime.now().strftime("%d/%m/%Y %H:%M")})
        st.rerun()

# Hiển thị bình luận
for c in st.session_state.comments:
    st.markdown(f"""
        <div style='background-color: #F3F4F6; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #1E40AF;'>
            <strong style='color: #1E40AF !important;'>👤 {c['name']}</strong> <small style='color: #6B7280;'>({c['time']})</small><br>
            <p style='color: #1A1A1A !important; margin-top: 5px;'>{c['text']}</p>
        </div>
    """, unsafe_allow_html=True)
