"""Gộp DiemThi_CaoHoc_K35.csv vào template.html -> index.html (một file tự chứa)."""
import csv, json, sys

src, tpl, out = sys.argv[1:4]
rows = list(csv.DictReader(open(src, encoding='utf-8-sig')))

def idx(lst, v):
    if v not in lst:
        lst.append(v)
    return lst.index(v)

places, majors, rooms, data = [], [], [], []
for x in rows:
    d, m, y = x['Ngày sinh'].split('/')
    dob = f'{int(d):02d}/{int(m):02d}/{y}' if d and m else x['Ngày sinh']  # có bản ghi thiếu tháng
    k = x['KTTH'].strip()
    data.append([
        x['Số báo danh'], x['Mã đăng ký'], x['Họ tên'],
        1 if x['Giới tính'] == 'Nữ' else 0,
        dob,
        idx(places, x['Nơi sinh']), idx(majors, x['Chuyên ngành']), idx(rooms, x['Phòng thi']),
        1 if x['Ngoại ngữ'] == 'Miễn NN' else 0,
        float(x['Môn luận']), None if k in ('---', '') else float(k), float(x['Điểm xét tuyển']),
        1 if x['Ghi chú'].strip() == 'Ưu tiên' else 0,
    ])

payload = json.dumps({'places': places, 'majors': majors, 'rooms': rooms, 'rows': data},
                     ensure_ascii=False, separators=(',', ':'))
html = open(tpl, encoding='utf-8').read().replace('/*__DATA__*/null', payload)
open(out, 'w', encoding='utf-8').write(html)
print(len(data), 'rows ->', out, len(html), 'bytes')
