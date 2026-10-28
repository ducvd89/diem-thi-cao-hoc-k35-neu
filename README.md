# Điểm thi Cao học Khóa 35 — ĐH Kinh tế Quốc dân (Đợt 2/2026)

Dữ liệu tổng hợp từ cổng tra cứu [tuyensinhsdh.neu.edu.vn](https://tuyensinhsdh.neu.edu.vn/KetQuaThi/CaoHoc). Tổng **1.316** thí sinh.

| File | Nội dung |
|---|---|
| `DiemThi_CaoHoc_K35.csv` | Bảng điểm đầy đủ (SBD, họ tên, ngành, điểm luận, KTTH, điểm xét tuyển…) |
| `ThongKe_CaoHoc_K35.csv` | Thống kê tổng hợp theo điểm, giới tính, ngành |

*Điểm công bố đã cộng điểm ưu tiên (1đ môn cơ bản) và trừ điểm vi phạm quy chế.*

## Trang web thống kê, tra cứu & xếp hạng

> ⚠️ **Lưu ý:** điểm chuẩn chính thức lấy từ thông báo ngày 27/10/2026 của Viện Đào tạo Sau đại học. Kết quả của từng thí sinh do trang tự suy ra từ điểm chuẩn và cách gán chuyên ngành → ngành (hoặc dự đoán theo chỉ tiêu), **không phải danh sách trúng tuyển chính thức** của nhà trường. Kết quả chính thức xem tại thông báo của ĐH Kinh tế Quốc dân.

Xem trực tuyến: https://ducvd89.github.io/diem-thi-cao-hoc-k35-neu/

Mở [`web/index.html`](web/index.html) bằng trình duyệt (một file duy nhất, chạy không cần mạng). Trang có các tab:

- **Tổng quan** — số liệu chính, kết quả xét tuyển (trúng tuyển / không đạt điểm chuẩn / điểm liệt / vắng), phổ điểm xét tuyển / Môn luận / KTTH, phân vị, ngưỡng Top N, Top 20.
- **Tra cứu** — tìm theo SBD, mã đăng ký hoặc họ tên (gõ không dấu được); hạng toàn khóa, trong ngành, trong phòng thi; kết quả xét tuyển theo điểm chuẩn.
- **Xếp hạng** — lọc theo ngành, chuyên ngành, giới tính, nơi sinh, phòng thi…; sắp xếp mọi cột, tên sắp theo chuẩn tiếng Việt (Tên → Họ → Đệm); tải CSV.
- **Trúng tuyển** — mặc định dùng điểm chuẩn chính thức của 13 ngành (công bố 27/10/2026), so sánh với điểm chuẩn dự đoán theo chỉ tiêu 624 của 14 ngành; loại thí sinh bị điểm liệt (có môn dưới 5); chỉnh được cách gán chuyên ngành → ngành và các giả định của chế độ dự đoán. *Danh sách từng thí sinh chỉ mang tính tham khảo, không phải danh sách chính thức.*
- **Chuyên ngành**, **Phân tích**, **Phòng thi** — thống kê chi tiết theo từng nhóm, kèm số và tỷ lệ trúng tuyển.

Tạo lại trang khi dữ liệu thay đổi:

```bash
python3 web/build/build.py DiemThi_CaoHoc_K35.csv web/build/template.html web/index.html
```
