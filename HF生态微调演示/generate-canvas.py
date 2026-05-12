"""
Latent Architecture · 大模型微调原理与实战研究报告
Redesigned — proper Chinese typography, refined layout
"""
import os
from reportlab.lib.pagesizes import landscape
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── font paths ──
WF     = r"C:/Windows/Fonts"
SKILL  = r"C:/Users/pan/.claude/plugins/cache/anthropic-agent-skills/document-skills/d230a6dd6eb1/skills/canvas-design/canvas-fonts"
OUT    = r"D:/vscode/document/HF生态微调演示"

# ── register fonts ──
def reg(name, path):
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(name, path))
    else:
        print(f"  MISSING: {path}")

# Chinese
reg("NotoSerifSC",   f"{WF}/NotoSerifSC-VF.ttf")
reg("NotoSansSC",    f"{WF}/NotoSansSC-VF.ttf")
reg("SimHei",        f"{WF}/simhei.ttf")
reg("YaHei",         f"{WF}/msyh.ttc")
reg("YaHeiBold",     f"{WF}/msyhbd.ttc")

# Latin
reg("CrimsonBold",   f"{SKILL}/CrimsonPro-Bold.ttf")
reg("CrimsonReg",    f"{SKILL}/CrimsonPro-Regular.ttf")
reg("InstrSans",     f"{SKILL}/InstrumentSans-Regular.ttf")
reg("InstrSansBold", f"{SKILL}/InstrumentSans-Bold.ttf")
reg("JetBrainsMono", f"{SKILL}/JetBrainsMono-Regular.ttf")
reg("JetBrainsBold", f"{SKILL}/JetBrainsMono-Bold.ttf")

# ── palette ──
BG      = HexColor("#131517")
SURFACE = HexColor("#1B1D20")
SURF2   = HexColor("#24272B")
AMBER   = HexColor("#D4872F")
RUST    = HexColor("#B85C3A")
ACCENT  = HexColor("#4A6FA5")
GREEN   = HexColor("#3A7A5C")
TEXT    = HexColor("#E8E4DA")
TEXT2   = HexColor("#A09C94")
TEXT3   = HexColor("#6A665E")
LINE    = HexColor("#2E3237")
LINE2   = HexColor("#3D4248")
GOLD    = HexColor("#C49A3C")

W, H = 1920, 1080
M = 80  # margin

class Canvas:
    def __init__(self, c):
        self.c = c
        c.setPageSize((W, H))

    # ── utilities ──
    def bg(self):
        c = self.c
        c.setFillColor(BG)
        c.rect(0, 0, W, H, fill=1, stroke=0)

    def vignette(self):
        c = self.c
        for i in range(80):
            a = 0.0025 * (1 - i/80)
            c.setFillColor(Color(0,0,0,alpha=a))
            m = i*2
            c.rect(m, m, W-2*m, H-2*m, fill=1, stroke=0)

    def corner(self, x, y, s=16):
        c = self.c
        c.setStrokeColor(LINE2)
        c.setLineWidth(1)
        c.line(x, y, x+s, y)
        c.line(x, y, x, y+s)

    def hrule(self, x, y, w, col=LINE):
        c = self.c
        c.setStrokeColor(col)
        c.setLineWidth(0.5)
        c.line(x, y, x+w, y)

    def grid(self, x, y, cols, rows, cw, rh, col=LINE):
        c = self.c
        c.setStrokeColor(col)
        c.setLineWidth(0.3)
        for i in range(cols+1):
            c.line(x+i*cw, y, x+i*cw, y+rows*rh)
        for j in range(rows+1):
            c.line(x, y+j*rh, x+cols*cw, y+j*rh)

    def rect_fill(self, x, y, w, h, r=0, col=SURF2):
        c = self.c
        c.setFillColor(col)
        if r:
            c.roundRect(x, y, w, h, r, fill=1, stroke=0)
        else:
            c.rect(x, y, w, h, fill=1, stroke=0)

    # ── typography shortcuts ──
    def title_cn(self, x, y, text, size=36, col=TEXT):
        c = self.c
        c.setFont("NotoSerifSC", size)
        c.setFillColor(col)
        c.drawString(x, y, text)

    def title_en(self, x, y, text, size=32, col=TEXT):
        c = self.c
        c.setFont("CrimsonBold", size)
        c.setFillColor(col)
        c.drawString(x, y, text)

    def body(self, x, y, text, size=13, col=TEXT2):
        c = self.c
        c.setFont("NotoSansSC", size)
        c.setFillColor(col)
        c.drawString(x, y, text)

    def mono(self, x, y, text, size=10, col=TEXT3):
        c = self.c
        c.setFont("JetBrainsMono", size)
        c.setFillColor(col)
        c.drawString(x, y, text)

    def accent(self, x, y, text, size=13, col=AMBER):
        c = self.c
        c.setFont("NotoSansSC", size)
        c.setFillColor(col)
        c.drawString(x, y, text)

    # ── page 1: cover ──
    def cover(self):
        c = self.c
        self.bg(); self.vignette()

        # large ghost text
        c.setFont("CrimsonBold", 300)
        c.setFillColor(Color(0.12, 0.13, 0.14, alpha=0.35))
        c.drawString(60, 180, "FT")

        # top annotation
        self.mono(1510, 1010, "TECHNICAL ANALYSIS  ·  2026", 9, TEXT3)
        self.mono(1510, 997, "REPORT  ·  ARCHITECTURE STUDY", 8, TEXT3)

        # corner marks
        for (dx, dy) in [(0,0), (1,0), (0,1), (1,1)]:
            cx = 50 + dx*(W-100)
            cy = 50 + dy*(H-100)
            self.corner(cx, cy)

        # headline
        self.title_cn(80, 740, "大模型微调原理与实战研究报告", 52)
        self.title_en(80, 680, "Fine-Tuning Principles & Practice", 28)

        # separator
        self.hrule(80, 645, 200, AMBER)

        # subtitle
        self.body(80, 605, "从原理到实战的完整指南  ·  基于开源项目实现本地大模型微调", 15, TEXT2)
        self.body(80, 578, "涵盖框架: LLaMA-Factory  ·  Unsloth  ·  Axolotl", 13, TEXT3)

        # metrics row
        metrics = [
            ("400+", "模型架构"),
            ("99.6%", "参数节约"),
            ("2x", "加速比"),
            ("~6 GB", "7B QLoRA"),
        ]
        for i, (num, lbl) in enumerate(metrics):
            x = 80 + i*240
            c.setFont("CrimsonBold", 42)
            c.setFillColor(AMBER if i != 2 else RUST)
            c.drawString(x, 480, num)
            self.body(x, 450, lbl, 11, TEXT3)

        # bottom grid
        self.grid(80, 80, 6, 4, 48, 48, LINE)
        self.mono(80, 55, "LATENT ARCHITECTURE  ·  HIDDEN STRUCTURES REVEALED", 8, TEXT3)
        c.showPage()

    # ── page 2: overview ──
    def overview(self):
        c = self.c
        self.bg(); self.vignette()
        self.corner(50, 1030); self.corner(1870, 1030)
        self.corner(50, 50); self.corner(1870, 50)

        self.title_cn(80, 970, "大模型微调概述", 34)
        self.title_en(80, 935, "Why Fine-Tune?", 18, AMBER)
        self.hrule(80, 915, 120, AMBER)

        # left: why fine-tune
        reasons = [
            ("领域适配", "医疗 / 法律 / 金融等专业知识需求"),
            ("风格控制", "特定输出格式与表达方式"),
            ("知识更新", "注入训练截止日期后的新知识"),
            ("指令遵循", "提升对特定指令格式的响应"),
            ("性能提升", "在特定任务上超越基座模型"),
        ]
        for i, (title, desc) in enumerate(reasons):
            y = 860 - i*60
            self.rect_fill(80, y-12, 520, 46, 4)
            self.title_cn(100, y+10, title, 16, AMBER)
            self.body(240, y+10, desc, 12, TEXT2)

        # right: comparison ladder
        ladder = [
            ("Prompt Engineering", TEXT3),
            ("RAG", TEXT3),
            ("Prompt Tuning", TEXT3),
            ("LoRA / QLoRA", AMBER),
            ("Full Fine-Tuning", RUST),
            ("RLHF / DPO", ACCENT),
        ]
        c.setFont("NotoSansSC", 13)
        c.setFillColor(TEXT2)
        c.drawString(740, 860, "技术路线对比")

        for i, (label, col) in enumerate(ladder):
            y = 825 - i*58
            self.rect_fill(740, y-14, 400, 42, 4, SURF2 if col==TEXT3 else SURF2)
            c.setStrokeColor(col)
            c.setLineWidth(3 if col!=TEXT3 else 1)
            c.line(740, y+11, 760, y+11)
            c.setFont("NotoSansSC" if col==TEXT3 else "SimHei", 14)
            c.setFillColor(col)
            c.drawString(770, y+2, label)
            if i < len(ladder)-1:
                c.setStrokeColor(LINE)
                c.setLineWidth(0.3)
                c.line(750, y-14, 750, y-56)

        # right panel: key data
        stats = [
            ("50+ GB", "预训练数据量级"),
            ("99%+", "参数量节约比例"),
            ("~6 GB", "消费级 GPU 微调门槛"),
            ("100+", "LLaMA-Factory 模型支持数"),
        ]
        c.setFont("NotoSansSC", 13)
        c.setFillColor(TEXT2)
        c.drawString(1280, 860, "关键数据")

        for i, (num, desc) in enumerate(stats):
            y = 820 - i*68
            c.setFont("CrimsonBold", 28)
            c.setFillColor(AMBER)
            c.drawString(1280, y, num)
            self.body(1280, y-22, desc, 11, TEXT3)

        # bottom annotation
        self.mono(80, 60, "FINE-TUNING: 在预训练基座上通过特定领域数据定向优化模型能力", 9, TEXT3)
        self.grid(1500, 60, 4, 3, 60, 60, LINE)
        c.showPage()

    # ── page 3: LoRA core ──
    def lora_core(self):
        c = self.c
        self.bg(); self.vignette()
        self.corner(50, 1030); self.corner(1870, 1030)
        self.corner(50, 50); self.corner(1870, 50)

        self.title_cn(80, 970, "LoRA 低秩适配", 34)
        self.title_en(80, 935, "Low-Rank Adaptation — Core Mathematics", 18, AMBER)
        self.hrule(80, 915, 120, AMBER)

        # left: formula area
        c.setFont("CrimsonBold", 20)
        # Let me use a different approach for the formula
        c.setFont("CrimsonBold", 20)
        c.setFillColor(TEXT)
        c.drawString(80, 850, "W₀  ∈  ℝᵈˣᵏ  →  ΔW = BA")

        c.setFont("CrimsonBold", 16)
        c.setFillColor(AMBER)
        c.drawString(80, 810, "W_new  =  W₀  +  α · BA / r")

        self.body(80, 775, "其中  r ≪ min(d, k)，A 随机高斯初始化，B 零初始化", 12, TEXT2)
        self.body(80, 752, "前向传播: y = W₀x + BAx，反向传播仅对 A、B 计算梯度", 12, TEXT2)
        self.body(80, 729, "推理时合并: W_merged = W₀ + α/r · BA，零额外延迟", 12, TEXT2)

        # matrix visualization
        def draw_grid(x, y, rows, cols, cell=22, gap=3, base_col=AMBER, label=""):
            c = self.c
            for r in range(rows):
                for col in range(cols):
                    px = x + col*(cell+gap)
                    py = y - r*(cell+gap)
                    v = 0.12 + 0.07 * ((r*cols+col) % 6)
                    clr = Color(base_col.red*v, base_col.green*v, base_col.blue*v)
                    c.setFillColor(clr)
                    c.rect(px, py-cell, cell, cell, fill=1, stroke=0)
            if label:
                self.mono(x, y-rows*(cell+gap)-8, label, 9, base_col)

        draw_grid(120, 720, 5, 5, 18, 2, ACCENT, "W₀  (冻结)")
        c.setFont("CrimsonBold", 28)
        c.setFillColor(TEXT3)
        c.drawString(270, 680, "=")
        draw_grid(300, 720, 5, 5, 18, 2, TEXT3, "W₀")
        c.setFont("CrimsonBold", 28)
        c.setFillColor(AMBER)
        c.drawString(440, 680, "+")
        draw_grid(470, 720, 5, 3, 18, 2, AMBER, "B  (r×k)")
        c.setFont("CrimsonBold", 20)
        c.setFillColor(TEXT3)
        c.drawString(585, 685, "×")
        draw_grid(610, 720, 3, 5, 18, 2, RUST, "A  (d×r)")

        # right: efficiency comparison
        self.title_cn(900, 850, "参数效率对比", 18)

        comps = [
            ("全量微调", "16,777,216", "100%", TEXT3, 1.0),
            ("LoRA r=8", "65,536", "99.6% ↓", AMBER, 0.004),
            ("LoRA r=16", "131,072", "99.2% ↓", GREEN, 0.008),
            ("LoRA r=64", "524,288", "96.9% ↓", RUST, 0.031),
        ]
        bar_max = 520
        for i, (method, params, saving, col, ratio) in enumerate(comps):
            y = 795 - i*72
            self.rect_fill(900, y-14, bar_max, 50, 6)
            bw = max(int(bar_max * ratio), 4)
            c.setFillColor(col)
            c.roundRect(900, y-14, bw, 50, 6, fill=1, stroke=0)

            c.setFont("NotoSansSC", 15)
            c.setFillColor(TEXT if i==0 else TEXT)
            c.drawString(920, y+8, method)
            c.setFont("JetBrainsMono", 10)
            c.setFillColor(TEXT3)
            c.drawString(920, y+26, params)
            c.setFont("CrimsonBold", 14)
            c.setFillColor(col)
            c.drawString(900+bar_max+24, y+14, saving)

        # bottom insight
        self.hrule(80, 370, 500)
        self.body(80, 345, "核心洞见：大模型在下游任务微调时的权重更新矩阵 ΔW 具有内在的低秩特性", 13, GOLD)
        self.body(80, 322, "这意味着 ΔW 可以用两个更小的矩阵的乘积来近似，从而大幅减少训练参数量", 12, TEXT3)

        c.showPage()

    # ── page 4: QLoRA & PEFT ──
    def qlora_peft(self):
        c = self.c
        self.bg(); self.vignette()
        self.corner(50, 1030); self.corner(1870, 1030)
        self.corner(50, 50); self.corner(1870, 50)

        self.title_cn(80, 970, "QLoRA 与 PEFT 方法全景", 34)
        self.title_en(80, 935, "Quantized Low-Rank Adaptation & Comparative Methods", 18, RUST)
        self.hrule(80, 915, 120, RUST)

        # three pillars of QLoRA
        pillars = [
            ("NF4 量化", "4-bit NormalFloat", "针对高斯分布定制的刻度表，\n权重密集区域精度更高", AMBER),
            ("双重量化", "Double Quantization", "对量化常数再做 8-bit 量化，\n进一步节省约 200MB", ACCENT),
            ("分页优化", "Paged Optimizer", "GPU 显存不足时自动转移\n至 CPU RAM，防止 OOM", GREEN),
        ]
        for i, (title, sub, desc, col) in enumerate(pillars):
            x = 80 + i*590
            self.rect_fill(x, 750, 540, 140, 8)
            c.setStrokeColor(col)
            c.setLineWidth(2)
            c.roundRect(x, 750, 540, 140, 8, fill=0, stroke=1)
            c.setFont("NotoSerifSC", 20)
            c.setFillColor(col)
            c.drawString(x+24, 840, title)
            self.body(x+24, 815, sub, 12, TEXT3)
            for li, line in enumerate(desc.split('\n')):
                self.body(x+24, 790-li*20, line, 11, TEXT2)

        # comparison table
        self.title_cn(80, 660, "LoRA vs QLoRA 性能对比", 18)
        table = [
            ("维度", "LoRA (BF16)", "QLoRA (4-bit)"),
            ("7B 显存", "~24 GB", "~6 GB"),
            ("13B 显存", "~48 GB", "~12 GB"),
            ("70B 显存", "~160 GB", "~48 GB"),
            ("训练速度", "1.0x", "0.6x"),
            ("效果评分", "98-99%", "97-98%"),
        ]
        col_xs  = [80, 300, 480]
        col_ws  = [220, 180, 180]
        row_h   = 38
        header_y = 620
        for i, row in enumerate(table):
            for j, cx in enumerate(col_xs):
                if i == 0:
                    self.rect_fill(cx-4, header_y-i*row_h, col_ws[j], row_h, 4 if j==0 else 0, SURFACE)
                    c.setFont("NotoSansSC" if j==0 else "JetBrainsBold", 11)
                    c.setFillColor(TEXT)
                else:
                    c.setFont("NotoSansSC" if j==0 else "JetBrainsMono", 11)
                    c.setFillColor(RUST if j==2 and "6" in row[j] else (AMBER if j==2 else TEXT2))
                c.drawString(cx+8, header_y-i*row_h+9, row[j])
            if i > 0:
                self.hrule(col_xs[0], header_y-i*row_h, col_ws[0]+col_ws[1]+col_ws[2], LINE)

        # right: PEFT methods
        self.title_cn(900, 660, "PEFT 方法对比", 18)

        peft = [
            ("Prompt Tuning", "~0.001%", "简单分类", TEXT3),
            ("Prefix Tuning", "~0.1%", "生成任务", TEXT3),
            ("P-Tuning v2", "~0.1-1%", "复杂 NLU", TEXT3),
            ("Adapter", "~0.5-8%", "多任务部署", TEXT3),
            ("LoRA", "~0.01-0.1%", "通用首选", AMBER),
            ("QLoRA", "~0.01-0.1%", "消费 GPU", RUST),
        ]
        for i, (name, params, scene, col) in enumerate(peft):
            y = 630 - i*40
            self.rect_fill(900, y-12, 500, 32, 4)
            c.setFont("NotoSansSC", 13 if col in [AMBER, RUST] else 12)
            c.setFillColor(col)
            c.drawString(920, y+4, name if col in [AMBER, RUST] else name)
            c.setFont("JetBrainsMono", 9)
            c.setFillColor(TEXT3)
            c.drawString(1080, y+4, params)
            c.setFont("NotoSansSC", 10)
            c.setFillColor(TEXT3)
            c.drawString(1200, y+4, scene)

        # selection guide
        self.hrule(80, 320, 700)
        c.setFont("NotoSansSC", 12)
        c.setFillColor(GOLD)
        c.drawString(80, 295, "选型建议:")
        self.body(80, 268, "简单文本分类 → Prompt Tuning  ·  复杂 NLU → LoRA  ·  文本生成 → Prefix Tuning / LoRA", 11, TEXT2)
        self.body(80, 245, "多任务部署 → Adapter  ·  显存受限 → QLoRA  ·  通用首选 → LoRA", 11, TEXT2)

        self.mono(80, 60, "QLoRA = 4-bit 量化基座 + 全精度 LoRA 适配器 · 显存降低 4-5 倍", 9, TEXT3)
        c.showPage()

    # ── page 5: six-layer stack ──
    def six_layer_stack(self):
        c = self.c
        self.bg(); self.vignette()
        self.corner(50, 1030); self.corner(1870, 1030)
        self.corner(50, 50); self.corner(1870, 50)

        self.title_cn(80, 970, "六层技术栈全景", 34)
        self.title_en(80, 935, "Architecture Stack — End-to-End Toolchain", 18, ACCENT)
        self.hrule(80, 915, 120, ACCENT)

        layers = [
            ("06", "LLaMA-Factory", "应用层 · 一站式微调框架", "100+ 模型", "#1A5C4A"),
            ("05", "TRL", "对齐层 · 强化学习对齐", "6+ 算法", "#C75B3A"),
            ("04", "PEFT", "效率层 · 参数高效微调", "10+ 方法", "#2E7D6B"),
            ("03", "Accelerate", "扩展层 · 分布式训练", "4 行接入", "#4A6FA5"),
            ("02", "Transformers", "模型层 · 核心模型库", "400+ 架构", "#8B6914"),
            ("01", "Datasets", "数据层 · 数据基础设施", "5 种模态", "#6B6B6B"),
        ]

        for i, (rank, name, desc, meta, hcolor) in enumerate(layers):
            y = 865 - i*92
            col = HexColor(hcolor)
            self.rect_fill(100, y-18, 1000, 68, 6)
            # left accent
            c.setFillColor(col)
            c.roundRect(100, y-18, 8, 68, 4, fill=1, stroke=0)
            # rank
            self.mono(124, y+20, rank, 12, TEXT3)
            # name
            c.setFont("NotoSerifSC", 20)
            c.setFillColor(col)
            c.drawString(160, y+20, name)
            # desc
            self.body(310, y+20, desc, 13, TEXT2)
            # meta
            c.setFont("JetBrainsMono", 11)
            c.setFillColor(TEXT2)
            c.drawString(1000-50, y+20, meta)

            # connector
            if i < len(layers)-1:
                c.setStrokeColor(LINE)
                c.setLineWidth(0.5)
                c.line(600, y-18, 600, y-86)

        # right panel: data highlights
        highlights = [
            ("400+", "模型架构", ACCENT),
            ("30+", "内置 Pipeline", ACCENT),
            ("0.01-1%", "参数更新比例", AMBER),
            ("3 种", "分布式后端", ACCENT),
            ("3 种", "Tokenizer 类型", ACCENT),
            ("5 种", "数据模态", TEXT2),
        ]
        self.title_cn(1280, 870, "关键数据", 16)
        for i, (num, label, col) in enumerate(highlights):
            y = 825 - i*62
            c.setFont("CrimsonBold", 30)
            c.setFillColor(col)
            c.drawString(1280, y, num)
            self.body(1280, y-24, label, 12, TEXT3)

        # frameworks
        self.title_cn(1280, 390, "上层框架", 16)
        fws = [
            ("LLaMA-Factory", "Web UI · 零代码", GREEN),
            ("Unsloth", "2x 加速 · 显存减半", AMBER),
            ("Axolotl", "YAML 配置 · 企业级", ACCENT),
        ]
        for i, (name, desc, col) in enumerate(fws):
            y = 355 - i*55
            self.rect_fill(1280, y-10, 480, 40, 6)
            c.setFillColor(col)
            c.roundRect(1280, y-10, 4, 40, 2, fill=1, stroke=0)
            c.setFont("NotoSerifSC", 15)
            c.setFillColor(TEXT)
            c.drawString(1300, y+8, name)
            self.body(1430, y+8, desc, 11, TEXT3)

        self.mono(80, 60, "STACK: Datasets → Transformers → Accelerate → PEFT → TRL → Application", 9, TEXT3)
        self.grid(80, 75, 3, 3, 60, 60, LINE)
        c.showPage()

    # ── page 6: frameworks comparison ──
    def framework_compare(self):
        c = self.c
        self.bg(); self.vignette()
        self.corner(50, 1030); self.corner(1870, 1030)
        self.corner(50, 50); self.corner(1870, 50)

        self.title_cn(80, 970, "三大框架对比选型", 34)
        self.title_en(80, 935, "LLaMA-Factory · Unsloth · Axolotl", 18, AMBER)
        self.hrule(80, 915, 120, AMBER)

        # three column layout
        cols = [
            ("LLaMA-Factory", GREEN, [
                "上手难度: ★☆☆", "Web UI, 零代码入门",
                "训练速度: 标准", "模型支持: 100+ 架构",
                "对齐方法: SFT/DPO/PPO", "Ollama 导出: 内置支持",
                "适合: 初学者/中级用户",
            ]),
            ("Unsloth", AMBER, [
                "上手难度: ★★☆", "Studio / Colab 界面",
                "训练速度: 2x 加速", "显存降低: 最高 70%",
                "对齐方法: SFT/DPO/GRPO", "模型支持: 500+",
                "适合: 中级/性能追求者",
            ]),
            ("Axolotl", ACCENT, [
                "上手难度: ★★★", "YAML 配置驱动",
                "训练速度: 标准", "分布式: FSDP/DeepSpeed",
                "对齐方法: DPO/GRPO/KTO", "企业级: 多节点/Slurm",
                "适合: 高级/企业用户",
            ]),
        ]

        for ci, (name, col, items) in enumerate(cols):
            cx = 80 + ci*580
            # card bg
            self.rect_fill(cx, 790, 520, 120, 8)
            # header
            c.setFillColor(col)
            c.roundRect(cx, 880, 520, 50, 8, fill=1, stroke=0)
            c.roundRect(cx, 870, 520, 10, 0, fill=1, stroke=0)  # flat bottom
            c.setFont("NotoSerifSC", 26)
            c.setFillColor(TEXT)
            c.drawString(cx+24, 893, name)

            # items
            for i, item in enumerate(items):
                y = 860 - i*38
                is_header = "难度" in item or "适合" in item
                c.setFont("NotoSansSC" if not is_header else "SimHei", 12)
                c.setFillColor(TEXT if is_header else TEXT2)
                prefix = "▹" if not is_header else ""
                c.drawString(cx+24, y+2, f"{prefix} {item}")

        # bottom recommendation
        self.hrule(80, 420, 500)
        c.setFont("NotoSansSC", 14)
        c.setFillColor(GOLD)
        c.drawString(80, 395, "推荐路线")

        recs = [
            ("初学者",     "→  LLaMA-Factory（Web UI 零代码入门）", GREEN),
            ("性能优先",   "→  Unsloth（2x 加速，显存减半）", AMBER),
            ("企业生产",   "→  Axolotl（分布式部署，生产环境）", ACCENT),
            ("进阶组合",   "→  LLaMA-Factory 处理数据 + Unsloth 训练 + Ollama 部署", TEXT2),
        ]
        for i, (who, rec, col) in enumerate(recs):
            y = 360 - i*36
            c.setFont("NotoSansSC", 12)
            c.setFillColor(col)
            c.drawString(100, y, f"{who}  {rec}")

        self.mono(80, 60, "CHOOSE YOUR FRAMEWORK: 入门选易用 · 性能选加速 · 生产选规模", 9, TEXT3)
        self.grid(80, 75, 3, 3, 60, 60, LINE)
        c.showPage()

    # ── page 7: data & hardware ──
    def data_hardware(self):
        c = self.c
        self.bg(); self.vignette()
        self.corner(50, 1030); self.corner(1870, 1030)
        self.corner(50, 50); self.corner(1870, 50)

        self.title_cn(80, 970, "数据集与硬件配置", 34)
        self.title_en(80, 935, "Data Preparation · Hardware Requirements · Hyperparameters", 18, AMBER)
        self.hrule(80, 915, 120, AMBER)

        # data formats
        self.title_cn(80, 860, "数据集格式", 18)
        formats = [
            ("Alpaca 格式", "单轮指令任务（翻译/分类/代码/问答）",
             '{"instruction": "...", "input": "...", "output": "..."}', AMBER),
            ("ShareGPT 格式", "多轮对话/角色扮演/Agent",
             '[{"from": "human", "value": "..."}, {"from": "gpt", "value": "..."}]', ACCENT),
        ]
        for i, (title, use, example, col) in enumerate(formats):
            x = 80 + i*460
            self.rect_fill(x, 750, 420, 90, 6)
            c.setStrokeColor(col)
            c.setLineWidth(1)
            c.roundRect(x, 750, 420, 90, 6, fill=0, stroke=1)
            c.setFont("NotoSansSC", 15)
            c.setFillColor(col)
            c.drawString(x+16, 808, title)
            self.body(x+16, 785, use, 10, TEXT3)
            self.mono(x+16, 758, example[:50]+"...", 8, TEXT3)

        # data quality pipeline
        self.title_cn(80, 680, "数据质量最佳实践", 16)
        pipeline = "原始数据  →  去重  →  长度过滤  →  语言检测  →  PII 脱敏  →  格式标准化"
        self.accent(80, 650, pipeline, 12, AMBER)

        tips = [
            "数据质量远重要于数据数量：5000 条高质量样本 > 10 万条噪声数据",
            "多样性优先：覆盖目标场景的各种变体",
            "人工校验种子集：先写 100-200 条高质量种子数据",
            "领域 : 通用数据 = 90 : 10，防止灾难性遗忘",
        ]
        for i, tip in enumerate(tips):
            self.body(80, 615-i*26, f"▹  {tip}", 11, TEXT2)

        # hardware
        self.title_cn(880, 860, "硬件需求速查", 18)
        hw = [
            ("入门", "1-4B QLoRA", "RTX 3060 12GB"),
            ("主流", "7-14B QLoRA", "RTX 4090 24GB"),
            ("进阶", "14-32B LoRA", "2× RTX 4090 48GB"),
            ("专业", "14-70B LoRA", "A100 80GB"),
            ("企业", "70-120B FT", "8× H100 640GB"),
        ]
        hx, hy = 880, 830
        header_row = ("预算", "可微调范围", "推荐硬件")
        for j, (hdr, cx) in enumerate(zip(header_row, [hx, hx+130, hx+290])):
            self.rect_fill(cx, hy-12, [120, 160, 180][j], 32, 4, SURFACE)
            c.setFont("NotoSansSC", 11)
            c.setFillColor(TEXT)
            c.drawString(cx+8, hy+4, hdr)

        for i, (lvl, scope, hw_name) in enumerate(hw):
            y = hy-12 - (i+1)*36
            col_vals = [lvl, scope, hw_name]
            for j, (val, cx) in enumerate(zip(col_vals, [hx, hx+130, hx+290])):
                self.rect_fill(cx, y, [120, 160, 180][j], 32)
                is_highlight = "4090" in val
                c.setFont("NotoSansSC", 11)
                c.setFillColor(AMBER if is_highlight else TEXT2)
                c.drawString(cx+8, y+8, val)

        # hyperparams
        self.title_cn(880, 570, "LoRA 关键超参数", 16)
        hp = [
            ("r (秩)", "8-128", "简单 r=8; 领域 r=32; 复杂 r=64"),
            ("alpha", "=r 或 2r", "控制微调力度"),
            ("dropout", "0.05-0.1", "防止过拟合"),
            ("learning_rate", "1e-5 ~ 5e-4", "LoRA 通常用 2e-4"),
            ("epochs", "3-10", "小数据多 epoch，大数据少 epoch"),
            ("batch_size", "1-8 + grad acc", "受显存限制"),
        ]
        for i, (param, rng, note) in enumerate(hp):
            y = 540 - i*38
            self.rect_fill(880, y-10, 500, 30, 4)
            c.setFont("JetBrainsMono", 10)
            c.setFillColor(AMBER)
            c.drawString(900, y+5, param)
            c.setFont("JetBrainsMono", 10)
            c.setFillColor(TEXT)
            c.drawString(1040, y+5, rng)
            self.body(1140, y+5, note, 9, TEXT3)

        self.mono(80, 60, "DATA QUALITY > DATA QUANTITY · 高质量数据是微调成功的核心", 9, TEXT3)
        self.grid(1600, 60, 3, 3, 60, 60, LINE)
        c.showPage()

    # ── page 8: cases & conclusion ──
    def cases_conclusion(self):
        c = self.c
        self.bg(); self.vignette()
        self.corner(50, 1030); self.corner(1870, 1030)
        self.corner(50, 50); self.corner(1870, 50)

        self.title_cn(80, 970, "实战案例与总结展望", 34)
        self.title_en(80, 935, "Practice Cases · Conclusion & Outlook", 18, GREEN)
        self.hrule(80, 915, 120, GREEN)

        # case studies
        cases = [
            ("案例一", "Qwen3-4B 现代诗风格微调", "LoRA + LLaMA-Factory", [
                "数据集: Iess/chinese_modern_poetry",
                "配置: lora/r=16, alpha=32, epochs=5",
                "部署: Ollama 导出 + Modelfile",
            ], AMBER),
            ("案例二", "Qwen3-14B 知识问答微调", "KTO 对齐", [
                "配置: lora/r=32, alpha=64, pref_loss=kto_pair",
                "显存: QLoRA 4-bit ~12 GB",
                "特点: 单条偏好标签, 数据量减半",
            ], ACCENT),
            ("案例三", "Qwen3-8B 端到端全流程", "数据→训练→部署", [
                "一键脚本: train_and_deploy.sh",
                "格式: Alpaca JSONL + dataset_info.json",
                "推荐 GPU: RTX 4090 (24 GB)",
            ], RUST),
        ]

        for i, (tag, title, method, items, col) in enumerate(cases):
            x = 80 + i*580
            self.rect_fill(x, 800, 520, 100, 8)
            c.setStrokeColor(col)
            c.setLineWidth(1)
            c.roundRect(x, 800, 520, 100, 8, fill=0, stroke=1)

            c.setFont("NotoSansSC", 11)
            c.setFillColor(col)
            c.drawString(x+16, 870, tag)
            c.setFont("NotoSerifSC", 17)
            c.setFillColor(TEXT)
            c.drawString(x+16, 845, title)
            c.setFont("JetBrainsMono", 10)
            c.setFillColor(TEXT3)
            c.drawString(x+16, 825, method)

            for j, item in enumerate(items):
                self.body(x+16, 790-j*22, f"▹ {item}", 10, TEXT2)

        # conclusion
        self.hrule(80, 450, 500, AMBER)
        self.title_cn(80, 420, "核心结论", 22, GOLD)

        conclusions = [
            "LoRA 是当前的最佳平衡点 —— 在效果、效率、易用性上均表现优异",
            "QLoRA 使消费级 GPU 微调成为现实 —— 4-bit 量化让 7B-14B 模型可在 RTX 4090 上微调",
            "数据质量远重要于数据数量 —— 5,000 条精心标注的数据往往优于 10 万条噪声数据",
            "开源工具链已成熟 —— Web UI → CLI → API 全覆盖，从入门到生产皆可",
        ]
        for i, text in enumerate(conclusions):
            y = 380 - i*38
            self.rect_fill(80, y-12, 1100, 32, 4)
            c.setFont("NotoSansSC", 12)
            c.setFillColor(TEXT2)
            c.drawString(100, y+4, f"0{i+1}  {text}")

        # outlook
        self.title_cn(80, 200, "趋势展望（2026）", 18, AMBER)
        trends = [
            "小型化：1-4B 小模型 + 微调 = 大模型 80%+ 效果",
            "偏好对齐：SFT → DPO/KTO/GRPO 成为标准流程",
            "端侧部署：GGUF 量化部署到手机和边缘设备",
            "自动化数据：LLM 自动生成 + 过滤高质量训练数据",
            "多模态微调：图文混合微调，应用场景扩展",
        ]
        for i, trend in enumerate(trends):
            self.body(80, 165-i*28, f"▹  {trend}", 11, TEXT3)

        # learning path
        self.title_cn(1280, 420, "推荐学习路径", 18, AMBER)
        phases = [
            ("入门", GREEN, [
                "理解 LoRA/QLoRA 原理",
                "LLaMA-Factory Web UI",
                "使用公开数据集",
            ]),
            ("进阶", AMBER, [
                "Alpaca/ShareGPT 格式",
                "自制领域数据集",
                "超参数调优",
            ]),
            ("生产", RUST, [
                "DPO/KTO 偏好对齐",
                "模型评估与部署",
                "分布式训练",
            ]),
        ]
        for i, (name, col, items) in enumerate(phases):
            y = 380 - i*110
            c.setFont("CrimsonBold", 16)
            c.setFillColor(col)
            c.drawString(1280, y, f"Phase {i+1}")
            c.setFont("NotoSansSC", 12)
            c.setFillColor(TEXT3)
            for j, item in enumerate(items):
                c.drawString(1280, y-22-j*24, f"▹ {item}")

        self.mono(80, 60, "LATENT ARCHITECTURE · 隐藏的结构即是美", 9, TEXT3)
        self.grid(1600, 60, 3, 3, 60, 60, LINE)
        c.showPage()


# ── main ──
out_path = os.path.join(OUT, "latent-architecture-report.pdf")
c = rl_canvas.Canvas(out_path, pagesize=(W, H))
p = Canvas(c)

p.cover()
p.overview()
p.lora_core()
p.qlora_peft()
p.six_layer_stack()
p.framework_compare()
p.data_hardware()
p.cases_conclusion()

c.save()
import os.path
sz = os.path.getsize(out_path)
print(f"OK Generated: {out_path}  ({sz//1024} KB, 8 pages)")
