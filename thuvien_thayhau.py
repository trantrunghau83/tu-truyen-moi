import streamlit as st
from datetime import datetime

# 1. CẤU HÌNH GIAO DIỆN PHONG CÁCH THƯ VIỆN
st.set_page_config(page_title="Thư Viện Số Thầy Hậu", page_icon="📚", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #FDF6E3; /* Màu giấy cũ */
    }
    .book-title {
        color: #5D4037;
        text-align: center;
        font-family: 'Times New Roman', serif;
        font-weight: bold;
        font-size: 40px;
        margin-bottom: 0px;
    }
    .chapter-box {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 5px;
        border: 1px solid #D7CCC8;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
        line-height: 1.8;
        font-size: 18px;
        color: #3E2723;
    }
    .comment-box {
        background-color: #EFEBE9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 5px solid #8D6E63;
    }
    .stButton>button {
        background-color: #8D6E63 !important;
        color: white !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. DỮ LIỆU SÁCH (Em đưa nội dung anh viết vào đây)
sach_du_lieu = {
    "Người Thầy Giữa Đời Thường": {
        "Lời nói đầu": """Có những con người không cần bước lên sân khấu lớn vẫn khiến người khác kính trọng... (Nội dung lời nói đầu của anh)""",
        "Chương 1: Tuổi thơ và ước mơ": """Ngày 7 tháng 9 năm 1978, tại phường Tân Lộc... (Nội dung chương 1)""",
        "Chương 2: Bước chân vào nghề": """Năm 2000, thầy Trần Trung Hậu chính thức bước vào nghề giáo...""",
        "Chương 5: Câu chuyện không thể quên": """Trong hành trình dạy học, có những niềm vui lớn, nhưng cũng có những nỗi buồn...""",
        # Anh có thể dán tiếp các chương khác vào đây
    },
    "Ký ức vùng đất Tân Lộc": {
        "Chương 1": "Nội dung quyển sách thứ 2 của anh sẽ nằm ở đây..."
    }
}

# 3. QUẢN LÝ BÌNH LUẬN (Mạng xã hội nhỏ)
if 'comments' not in st.session_state:
    st.session_state.comments = [
        {"name": "Học trò cũ", "content": "Em đọc mà xúc động quá thầy ơi, cảm ơn thầy vì những năm tháng dạy dỗ!", "time": "20/05/2024"},
        {"name": "Đồng nghiệp", "content": "Một tấm gương sáng cho thế hệ giáo viên trẻ noi theo.", "time": "21/05/2024"}
    ]

# 4. GIAO DIỆN CHÍNH
st.markdown("<h1 class='book-title'>📚 THƯ VIỆN SỐ THẦY HẬU</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #8D6E63;'>Nơi lưu giữ những ký ức và tri thức</p>", unsafe_allow_html=True)

# Chọn sách
chon_sach = st.sidebar.selectbox("📖 Chọn tác phẩm:", list(sach_du_lieu.keys()))

# Chọn chương
danh_sach_chuong = list(sach_du_lieu[chon_sach].keys())
chon_chuong = st.sidebar.radio("Chương sách:", danh_sach_chuong)

# Hiển thị nội dung
st.markdown(f"## {chon_chuong}")
st.markdown(f"<div class='chapter-box'>{sach_du_lieu[chon_sach][chon_chuong]}</div>", unsafe_allow_html=True)

st.markdown("---")

# 5. PHẦN BÌNH LUẬN (MẠNG XÃ HỘI)
st.subheader("💬 Bạn đọc nhận xét")

# Form gửi bình luận
with st.form("comment_form", clear_on_submit=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        ten = st.text_input("Tên của bạn:")
    with col2:
        noidung = st.text_area("Cảm nhận của bạn về tác phẩm:")
    
    submit = st.form_submit_button("Gửi nhận xét")
    if submit and ten and noidung:
        new_comment = {
            "name": ten,
            "content": noidung,
            "time": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        st.session_state.comments.insert(0, new_comment)
        st.success("Cảm ơn bạn đã chia sẻ cảm xúc!")
        st.rerun()

# Hiển thị danh sách bình luận
for c in st.session_state.comments:
    st.markdown(f"""
    <div class='comment-box'>
        <strong>{c['name']}</strong> <small style='color: #8D6E63;'>({c['time']})</small><br>
        {c['content']}
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("Đây là không gian chia sẻ những tác phẩm của Nhà giáo Ưu tú Trần Trung Hậu.")