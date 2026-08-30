# -*- coding: utf-8 -*-
"""So do nguyen ly do (SVG inline) chen vao bai viet / hub.

Moi so do la line-art sach, dung he mau thuong hieu, khong dinh ban quyen.
diagram_for(product)  -> chon so do theo product['tech'] hoac product['main'].
diagram_for_hub(hub)  -> chon so do theo hub['slug'].
"""

# --- he mau (dong bo voi site.css) ---
BLUE = "#177db2"; BLUED = "#0e4867"; INK = "#273237"; MUT = "#667983"
MAG = "#a8005c"; LIQ = "#d6ebf7"; LINE = "#c4d2da"; PAPER = "#ffffff"

_VESSEL = (
    '<rect x="60" y="70" width="300" height="250" rx="10" fill="{paper}" stroke="{ink}" stroke-width="2.5"/>'
).format(paper=PAPER, ink=INK)


def _wrap(title, svg_inner, vb="0 0 880 380", note=""):
    cap = '<strong>{t}</strong>'.format(t=title)
    if note:
        cap += ' ' + note
    return (
        '<figure class="article-diagram">'
        '<div class="diagram-stage">'
        '<svg viewBox="{vb}" role="img" aria-label="{t}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'
        '</div><figcaption>{cap}</figcaption></figure>'
    ).format(vb=vb, t=title, inner=svg_inner, cap=cap)


def _label(x, y, text, anchor="start", weight="600", color=None, size="17"):
    color = color or INK
    return ('<text x="{x}" y="{y}" font-family="Be Vietnam Pro,Arial,sans-serif" '
            'font-size="{s}" font-weight="{w}" fill="{c}" text-anchor="{a}">{t}</text>').format(
        x=x, y=y, s=size, w=weight, c=color, a=anchor, t=text)


# ------------------------------------------------------------------ RADAR
def _radar():
    liquid = '<rect x="62" y="230" width="296" height="88" rx="6" fill="{liq}"/>'.format(liq=LIQ)
    waves = ''.join(
        '<path d="M{x1} 110 A 60 60 0 0 1 {x2} 110" fill="none" stroke="{b}" stroke-width="2" opacity="{o}"/>'.format(
            x1=210 - r, x2=210 + r, b=BLUE, o=0.9 - i * 0.22)
        for i, r in enumerate([34, 58, 82]))
    inner = (
        _VESSEL + liquid +
        # flange + sensor
        '<rect x="188" y="46" width="44" height="26" rx="3" fill="{blued}"/>'.format(blued=BLUED) +
        '<rect x="196" y="30" width="28" height="20" rx="3" fill="{ink}"/>'.format(ink=INK) +
        waves +
        # beam down to surface
        '<line x1="210" y1="72" x2="210" y2="228" stroke="{b}" stroke-width="2.5" stroke-dasharray="2 6"/>'.format(b=BLUE) +
        '<polygon points="210,232 204,218 216,218" fill="{b}"/>'.format(b=BLUE) +
        # surface line
        '<line x1="62" y1="230" x2="358" y2="230" stroke="{mag}" stroke-width="2.5"/>'.format(mag=MAG) +
        # distance arrow
        '<line x1="330" y1="72" x2="330" y2="230" stroke="{mut}" stroke-width="1.5"/>'.format(mut=MUT) +
        '<polygon points="330,72 326,84 334,84" fill="{mut}"/><polygon points="330,230 326,218 334,218" fill="{mut}"/>'.format(mut=MUT) +
        # labels
        _label(420, 52, "Cảm biến radar 80 GHz", size="18") +
        _label(420, 84, "Phát sóng vi ba xuống bề mặt", color=MUT, weight="400") +
        _label(420, 150, "Đo thời gian sóng phản xạ", color=MUT, weight="400") +
        _label(420, 200, "→ suy ra khoảng cách rồi tính mức", color=MUT, weight="400") +
        _label(420, 250, "Bề mặt chất lỏng phản xạ", color=MAG) +
        _label(210, 345, "Không tiếp xúc môi chất", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý đo mức radar không tiếp xúc (Micropilot)", inner)


# ------------------------------------------------------------------ TDR / guided radar
def _tdr():
    liquid = '<rect x="62" y="240" width="296" height="78" rx="6" fill="{liq}"/>'.format(liq=LIQ)
    inner = (
        _VESSEL + liquid +
        '<rect x="196" y="46" width="28" height="26" rx="3" fill="{blued}"/>'.format(blued=BLUED) +
        # probe rod
        '<line x1="210" y1="72" x2="210" y2="308" stroke="{ink}" stroke-width="4"/>'.format(ink=INK) +
        # pulses along probe
        ''.join('<circle cx="210" cy="{cy}" r="6" fill="none" stroke="{b}" stroke-width="2"/>'.format(cy=cy, b=BLUE)
                for cy in [100, 140, 180]) +
        '<line x1="62" y1="240" x2="358" y2="240" stroke="{mag}" stroke-width="2.5"/>'.format(mag=MAG) +
        '<circle cx="210" cy="240" r="9" fill="none" stroke="{mag}" stroke-width="2.5"/>'.format(mag=MAG) +
        _label(420, 52, "Radar dẫn sóng TDR (Levelflex)", size="18") +
        _label(420, 90, "Xung điện từ chạy dọc que / cáp", color=MUT, weight="400") +
        _label(420, 150, "Phản xạ mạnh tại bề mặt môi chất", color=MUT, weight="400") +
        _label(420, 250, "Điểm phản xạ = mức đo", color=MAG) +
        _label(210, 345, "Hợp môi chất điện môi thấp, bồn hẹp, có bọt", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý radar dẫn sóng TDR (Levelflex)", inner)


# ------------------------------------------------------------------ ULTRASONIC
def _ultrasonic():
    liquid = '<rect x="62" y="240" width="296" height="78" rx="6" fill="{liq}"/>'.format(liq=LIQ)
    waves = ''.join(
        '<path d="M{x1} 120 A 55 55 0 0 1 {x2} 120" fill="none" stroke="{b}" stroke-width="2" opacity="{o}"/>'.format(
            x1=210 - r, x2=210 + r, b=BLUE, o=0.85 - i * 0.2)
        for i, r in enumerate([30, 52, 74]))
    inner = (
        _VESSEL + liquid +
        '<rect x="190" y="44" width="40" height="28" rx="4" fill="{blued}"/>'.format(blued=BLUED) +
        # blind zone
        '<rect x="150" y="72" width="120" height="34" fill="{mut}" opacity="0.12"/>'.format(mut=MUT) +
        waves +
        '<line x1="210" y1="72" x2="210" y2="238" stroke="{b}" stroke-width="2" stroke-dasharray="2 6"/>'.format(b=BLUE) +
        '<line x1="62" y1="240" x2="358" y2="240" stroke="{mag}" stroke-width="2.5"/>'.format(mag=MAG) +
        _label(420, 52, "Đầu dò siêu âm (Prosonic)", size="18") +
        _label(420, 90, "Phát xung âm, đo thời gian truyền — về", color=MUT, weight="400") +
        _label(420, 150, "Vùng chết ngay dưới đầu dò", color=MUT, weight="400") +
        _label(420, 250, "Bề mặt phản xạ sóng âm", color=MAG) +
        _label(210, 345, "Kinh tế cho nước, nước thải, chất rắn rời", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý đo mức siêu âm (Prosonic)", inner)


# ------------------------------------------------------------------ HYDROSTATIC
def _hydrostatic():
    liquid = '<rect x="62" y="150" width="296" height="168" rx="6" fill="{liq}"/>'.format(liq=LIQ)
    inner = (
        _VESSEL + liquid +
        '<line x1="62" y1="150" x2="358" y2="150" stroke="{mag}" stroke-width="2.5"/>'.format(mag=MAG) +
        # sensor at bottom
        '<rect x="188" y="304" width="44" height="26" rx="4" fill="{blued}"/>'.format(blued=BLUED) +
        # height arrow
        '<line x1="120" y1="150" x2="120" y2="316" stroke="{mut}" stroke-width="1.5"/>'.format(mut=MUT) +
        '<polygon points="120,150 116,162 124,162" fill="{mut}"/><polygon points="120,316 116,304 124,304" fill="{mut}"/>'.format(mut=MUT) +
        _label(134, 240, "h", color=INK, size="18") +
        _label(420, 52, "Đo mức thủy tĩnh (Deltapilot / Waterpilot)", size="17") +
        _label(420, 96, "Áp suất cột chất lỏng tỉ lệ với mức", color=MUT, weight="400") +
        '<rect x="420" y="150" width="220" height="46" rx="6" fill="{paper}" stroke="{line}" stroke-width="1.5"/>'.format(paper=PAPER, line=LINE) +
        _label(530, 179, "p = ρ · g · h", anchor="middle", color=BLUED, size="20") +
        _label(420, 250, "Cảm biến áp đặt tại đáy bồn", color=MAG) +
        _label(210, 345, "ρ đổi theo tỉ trọng / nhiệt độ môi chất", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý đo mức thủy tĩnh (p = ρgh)", inner)


# ------------------------------------------------------------------ PRESSURE
def _pressure():
    inner = (
        # process pipe
        '<rect x="60" y="250" width="360" height="70" rx="8" fill="{liq}" stroke="{ink}" stroke-width="2.5"/>'.format(liq=LIQ, ink=INK) +
        '<text x="240" y="292" font-family="Be Vietnam Pro,Arial,sans-serif" font-size="16" fill="{mut}" text-anchor="middle">Đường ống / bồn quá trình</text>'.format(mut=MUT) +
        # transmitter body
        '<rect x="196" y="150" width="88" height="60" rx="8" fill="{paper}" stroke="{ink}" stroke-width="2.5"/>'.format(paper=PAPER, ink=INK) +
        '<circle cx="240" cy="180" r="20" fill="none" stroke="{blued}" stroke-width="2.5"/>'.format(blued=BLUED) +
        '<line x1="240" y1="180" x2="240" y2="166" stroke="{blued}" stroke-width="2"/><line x1="240" y1="180" x2="252" y2="184" stroke="{blued}" stroke-width="2"/>'.format(blued=BLUED) +
        # process connection + diaphragm
        '<rect x="228" y="210" width="24" height="40" fill="{blued}"/>'.format(blued=BLUED) +
        '<line x1="222" y1="250" x2="258" y2="250" stroke="{mag}" stroke-width="3"/>'.format(mag=MAG) +
        # pressure arrows up
        ''.join('<line x1="{x}" y1="300" x2="{x}" y2="258" stroke="{b}" stroke-width="2"/><polygon points="{x},254 {xm},266 {xp},266" fill="{b}"/>'.format(
            x=x, xm=x - 4, xp=x + 4, b=BLUE) for x in [210, 240, 270]) +
        # signal out
        '<line x1="284" y1="180" x2="470" y2="180" stroke="{ink}" stroke-width="2"/>'.format(ink=INK) +
        '<polygon points="474,180 462,175 462,185" fill="{ink}"/>'.format(ink=INK) +
        _label(500, 150, "Áp suất quá trình", size="18") +
        _label(500, 178, "→ màng cảm biến", color=MUT, weight="400") +
        _label(500, 206, "→ ô đo (gốm / piezoresistive)", color=MUT, weight="400") +
        _label(320, 176, "4–20 mA · HART", color=BLUED, size="15") +
        _label(275, 246, "Màng ngăn", anchor="start", color=MAG, size="14") +
        _label(240, 355, "Cerabar / Ceraphant", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý đo áp suất bằng màng cảm biến (Cerabar)", inner)


# ------------------------------------------------------------------ DIFFERENTIAL PRESSURE
def _dp():
    inner = (
        # tank
        _VESSEL.replace('width="300"', 'width="240"') +
        '<rect x="62" y="150" width="236" height="168" rx="6" fill="{liq}"/>'.format(liq=LIQ) +
        '<line x1="62" y1="150" x2="298" y2="150" stroke="{mag}" stroke-width="2.5"/>'.format(mag=MAG) +
        # high tap (bottom) and low tap (top)
        '<circle cx="80" cy="300" r="7" fill="{b}"/>'.format(b=BLUE) +
        '<circle cx="80" cy="96" r="7" fill="{blued}"/>'.format(blued=BLUED) +
        '<line x1="80" y1="300" x2="360" y2="300" stroke="{b}" stroke-width="2.5"/>'.format(b=BLUE) +
        '<line x1="80" y1="96" x2="360" y2="96" stroke="{blued}" stroke-width="2.5" stroke-dasharray="6 4"/>'.format(blued=BLUED) +
        # dp cell
        '<rect x="360" y="150" width="96" height="96" rx="10" fill="{paper}" stroke="{ink}" stroke-width="2.5"/>'.format(paper=PAPER, ink=INK) +
        '<line x1="408" y1="150" x2="408" y2="96" stroke="{blued}" stroke-width="2.5" stroke-dasharray="6 4"/>'.format(blued=BLUED) +
        '<line x1="408" y1="246" x2="408" y2="300" stroke="{b}" stroke-width="2.5"/>'.format(b=BLUE) +
        _label(408, 202, "Δp", anchor="middle", color=BLUED, size="22") +
        _label(500, 120, "Áp thấp (−)", color=BLUED, size="16") +
        _label(500, 300, "Áp cao (+)", color=BLUE, size="16") +
        _label(500, 190, "Chênh áp Δp = p₊ − p₋", size="17") +
        _label(500, 222, "→ mức / lưu lượng / áp suất", color=MUT, weight="400") +
        _label(260, 355, "Deltabar — đo chênh áp hai phía", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý đo chênh áp (Deltabar)", inner)


# ------------------------------------------------------------------ VIBRONIC fork
def _vibronic():
    liquid = '<rect x="62" y="235" width="296" height="83" rx="6" fill="{liq}"/>'.format(liq=LIQ)
    inner = (
        _VESSEL + liquid +
        '<line x1="62" y1="235" x2="358" y2="235" stroke="{mag}" stroke-width="2"/>'.format(mag=MAG) +
        # fork mounted on side, tines at threshold
        '<rect x="150" y="196" width="40" height="20" rx="3" fill="{blued}"/>'.format(blued=BLUED) +
        '<line x1="164" y1="216" x2="160" y2="262" stroke="{ink}" stroke-width="4"/>'.format(ink=INK) +
        '<line x1="176" y1="216" x2="180" y2="262" stroke="{ink}" stroke-width="4"/>'.format(ink=INK) +
        # vibration arcs
        '<path d="M150 240 q -10 -8 0 -16" fill="none" stroke="{b}" stroke-width="2"/>'.format(b=BLUE) +
        '<path d="M190 240 q 10 -8 0 -16" fill="none" stroke="{b}" stroke-width="2"/>'.format(b=BLUE) +
        _label(420, 52, "Công tắc mức kiểu rung (Liquiphant)", size="17") +
        _label(420, 92, "Ngã ba âm thoa dao động ở tần số riêng", color=MUT, weight="400") +
        _label(420, 150, "Ngập môi chất → tần số giảm", color=MUT, weight="400") +
        _label(420, 200, "→ chuyển trạng thái đóng/ngắt", color=MUT, weight="400") +
        _label(420, 250, "Ngưỡng báo mức", color=MAG) +
        _label(210, 345, "Tin cậy cho báo đầy / báo cạn, chức năng an toàn", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý công tắc mức kiểu rung (Liquiphant / Soliphant)", inner)


# ------------------------------------------------------------------ CAPACITANCE
def _capacitance():
    liquid = '<rect x="62" y="210" width="296" height="108" rx="6" fill="{liq}"/>'.format(liq=LIQ)
    inner = (
        _VESSEL + liquid +
        '<line x1="62" y1="210" x2="358" y2="210" stroke="{mag}" stroke-width="2"/>'.format(mag=MAG) +
        '<rect x="196" y="46" width="28" height="26" rx="3" fill="{blued}"/>'.format(blued=BLUED) +
        '<line x1="210" y1="72" x2="210" y2="300" stroke="{ink}" stroke-width="4"/>'.format(ink=INK) +
        # field between probe and wall
        ''.join('<line x1="210" y1="{y}" x2="358" y2="{y}" stroke="{b}" stroke-width="1.2" stroke-dasharray="3 6" opacity="0.7"/>'.format(y=y, b=BLUE)
                for y in [250, 275, 300]) +
        ''.join('<line x1="210" y1="{y}" x2="62" y2="{y}" stroke="{b}" stroke-width="1.2" stroke-dasharray="3 6" opacity="0.7"/>'.format(y=y, b=BLUE)
                for y in [250, 275, 300]) +
        _label(420, 52, "Công tắc / đo mức điện dung", size="18") +
        _label(420, 92, "Que làm một bản tụ, thành bồn là bản kia", color=MUT, weight="400") +
        _label(420, 150, "Mức đổi → điện dung đổi", color=MUT, weight="400") +
        _label(420, 250, "Điện trường que ↔ thành bồn", color=MAG) +
        _label(210, 345, "Phù hợp chất rắn, chất bám dính, giao diện", anchor="middle", color=MUT, weight="400", size="15")
    )
    return _wrap("Nguyên lý đo mức điện dung", inner)


# ------------------------------------------------------------------ TEMPERATURE
def _temperature():
    inner = (
        # process pipe
        '<rect x="60" y="60" width="90" height="300" rx="10" fill="{liq}" stroke="{ink}" stroke-width="2.5"/>'.format(liq=LIQ, ink=INK) +
        '<text x="105" y="350" font-family="Be Vietnam Pro,Arial,sans-serif" font-size="14" fill="{mut}" text-anchor="middle">Ống quá trình</text>'.format(mut=MUT) +
        # thermowell into pipe
        '<rect x="150" y="150" width="150" height="26" rx="6" fill="{blued}"/>'.format(blued=BLUED) +
        '<rect x="90" y="156" width="70" height="14" rx="4" fill="{ink}"/>'.format(ink=INK) +
        # RTD element inside
        '<line x1="110" y1="163" x2="150" y2="163" stroke="{mag}" stroke-width="3"/>'.format(mag=MAG) +
        '<circle cx="112" cy="163" r="5" fill="{mag}"/>'.format(mag=MAG) +
        # transmitter head
        '<rect x="300" y="128" width="90" height="70" rx="12" fill="{paper}" stroke="{ink}" stroke-width="2.5"/>'.format(paper=PAPER, ink=INK) +
        '<circle cx="345" cy="163" r="18" fill="none" stroke="{blued}" stroke-width="2.5"/>'.format(blued=BLUED) +
        # signal out
        '<line x1="390" y1="163" x2="470" y2="163" stroke="{ink}" stroke-width="2"/><polygon points="474,163 462,158 462,168" fill="{ink}"/>'.format(ink=INK) +
        _label(500, 120, "Điểm đo nhiệt độ gồm 3 phần:", size="17") +
        _label(500, 156, "Thermowell — ống bảo vệ", color=MUT, weight="400") +
        _label(500, 186, "Phần tử RTD Pt100 / cặp nhiệt", color=MAG) +
        _label(500, 216, "Bộ chuyển đổi iTEMP", color=MUT, weight="400") +
        _label(430, 150, "4–20 mA", color=BLUED, size="14")
    )
    return _wrap("Cấu tạo một điểm đo nhiệt độ (thermowell + RTD + iTEMP)", inner)


_BUILDERS = {
    "radar": _radar, "tdr": _tdr, "ultrasonic": _ultrasonic, "hydrostatic": _hydrostatic,
    "pressure": _pressure, "dp": _dp, "vibronic": _vibronic, "capacitance": _capacitance,
    "temperature": _temperature,
}

# slug (tech hoac main) -> khoa so do
_SLUG2KEY = {
    "radar-do-muc-micropilot": "radar",
    "radar-dan-song-levelflex": "tdr",
    "sieu-am-do-muc-prosonic": "ultrasonic",
    "do-muc-thuy-tinh-deltapilot-waterpilot": "hydrostatic",
    "cam-bien-ap-suat-cerabar-ceraphant": "pressure",
    "cam-bien-chenh-ap-deltabar": "dp",
    "cong-tac-muc-rung-liquiphant-soliphant": "vibronic",
    "cong-tac-muc-dien-dung-dan-dien": "capacitance",
    "bo-chuyen-doi-tin-hieu-nhiet-itemp": "temperature",
    "nhiet-ke-cong-nghiep-itherm-omnigrad": "temperature",
    # hub chinh -> so do dai dien
    "do-muc-endress-hauser": "radar",
    "do-ap-suat-endress-hauser": "pressure",
    "cong-tac-muc-endress-hauser": "vibronic",
    "do-nhiet-do-endress-hauser": "temperature",
}


def _key_for_slugs(*slugs):
    for s in slugs:
        if s and s in _SLUG2KEY:
            return _SLUG2KEY[s]
    return None


def diagram_for(product):
    if not product:
        return ""
    key = _key_for_slugs(product.get("tech"), product.get("main"))
    if not key:
        return ""
    return _BUILDERS[key]()


def diagram_for_hub(hub):
    key = _key_for_slugs(hub.get("slug"), hub.get("parent"))
    if not key:
        return ""
    return _BUILDERS[key]()
