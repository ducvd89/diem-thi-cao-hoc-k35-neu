# Điểm thi Cao học Khóa 35 — ĐH Kinh tế Quốc dân (Đợt 2/2026)

Dữ liệu tổng hợp từ cổng tra cứu [tuyensinhsdh.neu.edu.vn](https://tuyensinhsdh.neu.edu.vn/KetQuaThi/CaoHoc). Tổng **1.316** thí sinh.

| File | Nội dung |
|---|---|
| `DiemThi_CaoHoc_K35.csv` | Bảng điểm đầy đủ (SBD, họ tên, ngành, điểm luận, KTTH, điểm xét tuyển…) |
| `ThongKe_CaoHoc_K35.csv` | Thống kê tổng hợp theo điểm, giới tính, ngành |

*Điểm công bố đã cộng điểm ưu tiên (1đ môn cơ bản) và trừ điểm vi phạm quy chế.*

## Trang web thống kê, tra cứu & xếp hạng

> ⚠️ **Lưu ý:** kết quả trúng tuyển trên trang chỉ là **dự đoán dựa trên chỉ tiêu**, **không phải thông báo chính thức** của nhà trường. Kết quả chính thức xem tại thông báo của ĐH Kinh tế Quốc dân.

Xem trực tuyến: https://ducvd89.github.io/diem-thi-cao-hoc-k35-neu/

Mở [`web/index.html`](web/index.html) bằng trình duyệt (một file duy nhất, chạy không cần mạng). Trang có các tab:

- **Tổng quan** — số liệu chính, phổ điểm xét tuyển / Môn luận / KTTH, phân vị, ngưỡng Top N, Top 20.
- **Tra cứu** — tìm theo SBD, mã đăng ký hoặc họ tên (gõ không dấu được); hạng toàn khóa, trong ngành, trong phòng thi; kết quả xét tuyển dự kiến.
- **Xếp hạng** — lọc theo ngành, chuyên ngành, giới tính, nơi sinh, phòng thi…; sắp xếp mọi cột, tên sắp theo chuẩn tiếng Việt (Tên → Họ → Đệm); tải CSV.
- **Trúng tuyển (dự kiến)** — mô phỏng theo chỉ tiêu 624 của 14 ngành; loại thí sinh bị điểm liệt (có môn dưới 5); chỉnh được cách xử lý đồng điểm và cách gán chuyên ngành → ngành. *Chỉ mang tính tham khảo, không phải kết quả chính thức.*
- **Chuyên ngành**, **Phân tích**, **Phòng thi** — thống kê chi tiết theo từng nhóm.

Tạo lại trang khi dữ liệu thay đổi:

```bash
python3 web/build/build.py DiemThi_CaoHoc_K35.csv web/build/template.html web/index.html
```
