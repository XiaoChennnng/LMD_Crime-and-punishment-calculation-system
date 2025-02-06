import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QTextEdit, QVBoxLayout, QWidget, QPushButton, QLabel, QHBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, QMenu
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

# 定义灵梦岛法律条文
LAWS = {
    "民事类法律": [
        {
            "罪名": "公共场合裸露下体罪",
            "描述": "根据本条法律，在公共场合裸露下体，构成犯罪。",
            "监禁时长": 20,
            "罚款": 12000
        },
        {
            "罪名": "扰乱治安罪",
            "描述": "扰乱治安罪是指在公共场所或公共交通工具上，故意或恶意地进行下列行为之一，导致公共安宁被打扰或其他人受到困扰：\n"
                    "故意发出暴力或非暴力的威胁，以致他人感到恐惧。\n"
                    "故意制造噪音或进行滋扰，干扰他人的正常活动。\n"
                    "故意进行挑衅、蛊惑或激怒他人，引发冲突或纷争。",
            "监禁时长": 15,
            "罚款": 10000
        },
        {
            "罪名": "酒驾",
            "描述": "重罪：法定酒精浓度限制：梦幻岛将驾驶者的血液酒精浓度 (BAC) 限定为 120。若 BAC 超过此限制，将被认定为醉驾。\n"
                    "轻罪：法定酒精浓度限制：梦幻岛将驾驶者的血液酒精浓度 (BAC) 限定为 20。若 BAC 超过此限制，将被认定为酒驾。",
            "监禁时长": 30,  # 重罪
            "罚款": 15000   # 重罪
        },
        {
            "罪名": "无证驾驶",
            "描述": "根据本条法律，未持有有效的驾驶执照且驾驶机动车辆的行为，构成犯罪。",
            "监禁时长": 0,
            "罚款": 6000
        },
        {
            "罪名": "违规停车",
            "描述": "根据本条法律，机动车辆驾驶员不得在以下任何状况下停车：\n"
                    "阻塞车道并阻挡其他车辆的正常行驶；\n"
                    "完全阻塞任何城市的巷道；\n"
                    "阻碍停车场出入口；\n"
                    "停放在对向车道上；\n"
                    "停放在桥梁上或隧道内。\n"
                    "根据本条法律，机动车辆驾驶员在非公共区域的停车场内停车，应遵守该区域的相关负责人员的要求停车。在属于自己的私人财产内可以按照自己设计的规则进行停车，但不得阻碍任何公共道路和人行道。政府部门有权为其所管理或维护的设施制定停车规则；无论驾驶员是否离开车辆，且无论车辆发动机是否熄火，只要车辆未在行进中，即被视为“停车”。",
            "监禁时长": 0,
            "罚款": 5000
        },
        {
            "罪名": "诈骗罪",
            "描述": "根据本条法律，诈骗罪是指以非法占有为目的，使用欺骗方法，骗取的公私财物的行为。",
            "监禁时长": 10,  # 轻罪
            "罚款": 9000
        },
        {
            "罪名": "拒绝支付账单罪",
            "描述": "根据本条法律，在公职人员提供服务后未能当场结清账单或拒绝支付账单行为，构成犯罪。",
            "监禁时长": 10,
            "罚款": 6000
        },
        {
            "罪名": "虚假报告罪",
            "描述": "根据本法律，故意提供虚假信息或虚假情况给执法机构，使其相信犯罪已经发生，将被视为虚假报告犯罪。\n"
                    "恶作剧虚假报告犯罪：根据该法律，故意制造恶作剧、恶意虚假警报或虚假报告，以引起警察或其他执法机构的关注和响应，构成犯罪；（这包括但不限于恶作剧性地报告虚假绑架、武装袭击等情况）。",
            "监禁时长": 20,
            "罚款": 10000
        },
        {
            "罪名": "高速逆行",
            "描述": "根据本条法律，在高速公路逆行的，构成犯罪，若对方造成损失需进行赔偿。",
            "监禁时长": 12,
            "罚款": 6000
        },
        {
            "罪名": "行贿罪",
            "描述": "贿赂公职人员罪是指给予、承诺给予或收受任何物品、服务、利益或报酬，以影响公职人员在其职责范围内的决策或行为。这包括贿赂公职人员、官员或其他政府代表的行为。\n"
                    "根据本条法律，公职人员在履行职责期间，未经合法许可接受或索取任何物品、服务、利益、现金或报酬，构成犯罪。",
            "监禁时长": 20,
            "罚款": 15000
        },
        {
            "罪名": "蓄意破坏/盗窃他人物品罪",
            "描述": "根据本条法律，蓄意破坏/盗窃他人的财产和财物、车辆等且拒绝赔付修理账单的行为，构成犯罪。",
            "监禁时长": 12,  # 轻罪
            "罚款": 9000
        },
        {
            "罪名": "侮辱尸体罪",
            "描述": "恶意鞭打尸体，嘲讽，在尸体上跳舞等行为构成犯罪。",
            "监禁时长": 20,
            "罚款": 12000
        }
    ],
    "任务类法律": [
        {
            "罪名": "车辆走私罪",
            "描述": "根据本条法律，以非法方式走私车辆的，构成犯罪。",
            "监禁时长": 18,
            "罚款": 9000
        },
        {
            "罪名": "小型抢劫罪",
            "描述": "1. 便利店抢劫（只允许使用手枪/1-2人/抢劫成功 30,000$ 黑钱/黑帮加 1 分）\n"
                    "2. 麦克家抢劫（需要 4-5 人开启/抢劫成功 300,000$ 黑钱/黑帮加 3 分）\n"
                    "3. 北部银行抢劫（需要 3-4 人开启/抢劫成功 200,000$ 黑钱/黑帮加 2 分）",
            "监禁时长": 20,
            "罚款": 12000
        },
        {
            "罪名": "大型抢劫罪",
            "描述": "1. 太平洋抢劫（服务器一天一次/8 人以上开启/抢劫成功 1,000,000$ /警局人数比劫匪多 1 人（警局最少 10 人/匪徒最少 9 人/按特殊绑架罪判罚）\n"
                    "2. 神秘制毒点（需要 5-8 人开启/抢劫成功 500,000$ 黑钱/黑帮加 5 分）\n"
                    "3. 大型酒店（需要 9-12 人开启/抢劫成功 1,000,000$ 黑钱/黑帮加 8 分）",
            "监禁时长": 45,
            "罚款": 40000
        },
        {
            "罪名": "特殊绑架罪",
            "描述": "根据本条法律，随意抱起他人收到报警或他人不在线挂机状态抱起他人都算绑架罪，除公职抱新市民，将不熟悉的人抱离安全区都构成犯罪。",
            "监禁时长": 48,
            "罚款": 30000
        }
    ],
    "违禁品类法律": [
        {
            "罪名": "非法使用武器罪",
            "描述": "根据本条法律，蓄意以鲁莽的方式使用枪支进行射击，并可能会造成他人受伤或死亡的行为，构成犯罪；\n"
                    "根据本条法律，向建筑物、交通工具或公共设施使用枪支进行射击的行为，构成犯罪，持枪证没收；\n"
                    "造成他人受伤或死亡的行为，枪械没收，持枪证没收。",
            "监禁时长": 18,
            "罚款": 9000
        },
        {
            "罪名": "非法展示武器罪",
            "描述": "根据本条法律，手持、携带或向他人展示或挥舞任何枪支、刀具，构成犯罪（活动期间除外），持枪证没收。",
            "监禁时长": 12,
            "罚款": 6000
        },
        {
            "罪名": "持有非法武器罪",
            "描述": "根据本条法律，在背包里持有未办理持枪证的枪支，构成犯罪，执法人员查获时应及时没收。\n"
                    "执法人员或某些政府雇员在执勤时持有上述武器的行为，不构成犯罪。",
            "监禁时长": 6,
            "罚款": 6000
        },
        {
            "罪名": "非法持有管制物品罪",
            "描述": "根据本条法律，非法持有管制物品，构成犯罪；\n"
                    "管制物品包括但不限于：可卡因、大麻、明胶大麻、鸦片、冰毒、迷幻药、邮票、摇头丸等。",
            "监禁时长": 15,
            "罚款": 9000
        },
        {
            "罪名": "非法贩卖管制物品罪",
            "描述": "根据本条法律，非法贩卖管制物品，构成犯罪；\n"
                    "管制物品包括但不限于：可卡因、大麻、明胶大麻、鸦片、冰毒、迷幻药、邮票、摇头丸等。",
            "监禁时长": 15,
            "罚款": 9000
        },
        {
            "罪名": "经济犯罪",
            "描述": "根据本条法律，只要携带黑钱，均算经济犯罪。",
            "监禁时长": 15,
            "罚款": 9000
        }
    ],
    "袭击警察类法律": [
        {
            "罪名": "袭警罪",
            "描述": "暴力袭击警察的行为，构成犯罪；\n"
                    "使用枪支、管制刀具，或者以驾驶机动车撞击等手段，严重危及其人身安全的，构成犯罪。",
            "监禁时长": 15,
            "罚款": 25000
        },
        {
            "罪名": "挑衅警察罪",
            "描述": "根据本条法律，对警员作出不雅行为，如竖中指、恶意寻衅滋事；\n"
                    "在警局门口摩擦车胎，恶意干扰警员正常工作；\n"
                    "使用车辆恶意撞击警员车辆；\n"
                    "使用热武器对准警员，并无视警告等行为，均构成犯罪。",
            "监禁时长": 10,
            "罚款": 10000
        },
        {
            "罪名": "恶意杀警罪",
            "描述": "非任务类、民事类、刑事类、违禁品类的情况下，无故击杀警员一次；\n"
                    "非任务类、民事类、刑事类、违禁品类的情况下，无故击杀警员两次；\n"
                    "非任务类、民事类、刑事类、违禁品类的情况下，无故击杀警员三次。",
            "监禁时长": "无限",
            "罚款": 0
        }
    ],
    "刑事类法律": [
        {
            "罪名": "非法入侵禁区罪",
            "描述": "根据本条法律，未经事先授权，进入任何禁区，构成犯罪。上述区域包括但不限于暗区、警局、军火库、监狱、毒品区等。（不与非法持有管制物品罪同时处罚，如身上有毒品判非法持有管制物品罪，若无毒品判非法入侵禁区罪）",
            "监禁时长": 15,
            "罚款": 15000
        },
        {
            "罪名": "非法入侵罪",
            "描述": "根据本条法律，未经土地或建筑物所有者、租户或管理者的允许，在其土地、建筑物或禁止区域内擅自进入，并在财产所有人、代理人或执法人员告诫其离开后，仍拒绝离开的行为，构成犯罪。",
            "监禁时长": 12,
            "罚款": 9000
        },
        {
            "罪名": "入室盗窃罪",
            "描述": "根据本条法律，未经财产所有人、租客或代理人的许可，进入其所拥有的财产并盗窃财物的行为，构成犯罪。必须全额返还财产。",
            "监禁时长": 18,
            "罚款": 15000
        },
        {
            "罪名": "抢劫罪",
            "描述": "使用威胁、暴力或武器：在实施抢劫时，犯罪嫌疑人使用实际威胁、暴力或持有武器，以恐吓或强制受害人交出财物，无论是现金、贵重物品或其他财物，构成犯罪。",
            "监禁时长": 20,
            "罚款": 30000
        },
        {
            "罪名": "车辆盗窃罪",
            "描述": "根据本条法律，盗窃或占用他人财物或车辆的行为，构成犯罪。",
            "监禁时长": 12,
            "罚款": 6000
        },
        {
            "罪名": "重大盗窃车辆罪",
            "描述": "根据本条法律，盗窃或占用公职车辆的行为，构成犯罪。",
            "监禁时长": 24,
            "罚款": 15000
        },
        {
            "罪名": "损坏公职车辆罪",
            "描述": "根据本条法律，蓄意损坏公职的车辆或拒绝赔付修理账单的行为，构成犯罪。",
            "监禁时长": 18,
            "罚款": 12000
        },
        {
            "罪名": "入店行窃罪",
            "描述": "根据本条法律，在没有付款意图的情况下，从商店或其他产业试图盗窃或藏匿商品的行为，构成犯罪。",
            "监禁时长": 12,
            "罚款": 6000
        },
        {
            "罪名": "妨碍执法人员罪",
            "描述": "妨碍警察或其他执法人员执行合法任务，如拒绝配合调查、阻止逮捕或拘留、在调查时提供虚假信息等，构成犯罪。",
            "监禁时长": 20,
            "罚款": 16000
        },
        {
            "罪名": "冒充政府雇员罪",
            "描述": "政府雇员包括：如执法人员、医务人员、技工人员、政府人员或其他公职人员。\n"
                    "冒用政府标识或徽章：使用政府部门的标识徽章或名称，使人误以为自己是合法的政府工作人员。\n"
                    "虚假宣称：在没有获得授权的情况下，声称自己是政府部门的工作人员，以获取他人的信任或好处。\n"
                    "滥用政府身份：如果个人原本是政府雇员，但滥用其地位，以获得不当利益，也可以被指控为冒充政府雇员罪。",
            "监禁时长": 30,
            "罚款": 30000
        },
        {
            "罪名": "妨碍政府雇员执行公务罪",
            "描述": "妨碍政府雇员执行公务罪可以包括以下行为：\n"
                    "阻挠政府雇员：有意干扰或阻碍政府雇员执行他们的法定职责，例如拒绝提供所需的文件或信息，或以其他方式阻止政府雇员进行调查或执法行动。\n"
                    "恐吓或威胁政府雇员：通过言语、行为或其他方式，对政府雇员施加威胁、恐吓或暴力，以阻止他们执行公务。\n"
                    "虚假报告或误导：故意提供虚假的报告、陈述或信息，或以其他方式误导政府雇员，干扰他们履行公务。",
            "监禁时长": 30,
            "罚款": 30000
        },
        {
            "罪名": "逃避羁押罪",
            "描述": "逃避羁押罪是指在被合法羁押或拘留期间，故意逃离或试图逃离执法机构的监管。包括以下情况：\n"
                    "脱逃：指已被合法羁押或拘留的人逃离监狱、拘留所、看守所或其他执法机构的羁押设施。\n"
                    "逃跑：指已被合法羁押或拘留的人在被执法人员押送、运送或转移期间逃跑或试图逃跑。",
            "监禁时长": 30,
            "罚款": 60000
        },
        {
            "罪名": "协助逃避羁押罪",
            "描述": "根据本条法律，协助越狱罪是指帮助、教唆、提供工具或其他方式协助他人逃脱合法羁押的行为。这包括提供藏身之处、运输逃犯、提供逃脱所需的工具或其他形式的帮助。",
            "监禁时长": 15,
            "罚款": 15000
        },
        {
            "罪名": "销毁证据罪",
            "描述": "根据本条法律，故意销毁、隐藏或篡改可能作为证据的物品或文件的行为，构成犯罪。",
            "监禁时长": 18,
            "罚款": 15000
        },
        {
            "罪名": "藐视法庭罪",
            "描述": "干扰法庭的正常运作，如在法庭内不听从指令、无礼行为、扰乱法庭秩序等。",
            "监禁时长": 30,
            "罚款": 30000
        },
        {
            "罪名": "冒充律师罪",
            "描述": "根据本条法律，未经认证的律师或假扮律师的行为，构成犯罪。",
            "监禁时长": 30,
            "罚款": 60000
        },
        {
            "罪名": "妨碍司法罪",
            "描述": "根据本条法律规定，任何人故意妨碍、阻碍或干扰下列人员的正当行动，构成妨碍司法罪：\n"
                    "法庭、法官、检察官、律师或其他法庭工作人员在履行职责时。\n"
                    "执行正当搜查、逮捕、暂扣或扣押职责的执法官员。\n"
                    "其他司法机关的人员在履行职责时。",
            "监禁时长": 30,
            "罚款": 20000
        },
        {
            "罪名": "袭击公职罪",
            "描述": "根据本条法律，蓄意攻击、伤害上班期间持有工作标识的人员（技工、市政、医护、消防等）构成犯罪。\n"
                    "情节严重的，至公职人员死亡的，从重处罚。",
            "监禁时长": 20,
            "罚款": 20000
        },
        {
            "罪名": "滥用职权罪",
            "描述": "根据该法律规定，以下行为可能构成滥用职权罪：\n"
                    "当一个公职人员在行使其职权时，故意滥用其职务或以不当的方式行使职责，构成滥用公职罪。这包括利用其职务地位获取不正当的利益、违反职责或法律规定，或通过滥用职权来剥夺他人的合法权益。",
            "监禁时长": 30,
            "罚款": 15000
        },
        {
            "罪名": "煽动暴乱罪",
            "描述": "1. 鼓励或教唆他人参与暴力行为或违法行为，如煽动他人进行抢劫、破坏财产、袭击他人等；制造、传播或宣传暴力或煽动性言论或消息，以激发暴乱或破坏行为。\n"
                    "2. 组织或参与集会、示威或抗议活动时，故意煽动或引导他人采取暴力或违法行为。",
            "监禁时长": 20,
            "罚款": 15000
        },
        {
            "罪名": "故意杀人罪",
            "描述": "故意杀人罪是指有预谋和故意杀害他人的行为。",
            "监禁时长": 70,
            "罚款": 50000
        }
    ]
}

class LawSystemApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("灵梦岛罪罚计算系统         Powered by Tom Chen")
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon("TNT.ico"))  # 设置窗口图标

        # 主布局
        main_layout = QHBoxLayout()

        # 左侧布局
        left_widget = QWidget()
        left_layout = QVBoxLayout()

        # 罪名列表
        self.law_list = QTreeWidget()
        self.law_list.setColumnCount(1)
        self.law_list.setHeaderLabels(["罪名"])
        self.law_list.setAlternatingRowColors(True)
        self.law_list.itemClicked.connect(self.on_law_item_clicked)

        # 添加法律类别
        for category, laws in LAWS.items():
            category_item = QTreeWidgetItem(self.law_list)
            category_item.setText(0, category)
            for law in laws:
                law_item = QTreeWidgetItem(category_item)
                law_item.setText(0, law["罪名"])
                law_item.setData(0, Qt.UserRole, law)  # 存储法律数据

        left_layout.addWidget(self.law_list)

        # 详细描述框
        self.description_box_label = QLabel("罪名详细描述")
        self.description_box = QTextEdit()
        self.description_box.setReadOnly(True)
        left_layout.addWidget(self.description_box_label)
        left_layout.addWidget(self.description_box)

        left_widget.setLayout(left_layout)

        # 右侧布局
        right_widget = QWidget()
        right_layout = QVBoxLayout()

        # 选中的罪名表格
        self.selected_crimes_table_label = QLabel("已选中罪名")
        self.selected_crimes_table = QTableWidget()
        self.selected_crimes_table.setColumnCount(3)
        self.selected_crimes_table.setHorizontalHeaderLabels(["罪名", "监禁时长", "罚款"])
        self.selected_crimes_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.selected_crimes_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selected_crimes_table.setStyleSheet("QTableWidget::item { text-align: center; }")
        self.selected_crimes_table.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 多选


        right_layout.addWidget(self.selected_crimes_table_label)
        right_layout.addWidget(self.selected_crimes_table)

        # 罚单备注和总计
        self.fine_slip_label = QLabel("罚单备注（可直接复制在游戏中 填写罚单理由）")
        self.fine_slip_text = QTextEdit()
        self.fine_slip_text.setReadOnly(True)
        self.fine_slip_text.setAcceptDrops(False)
        self.fine_slip_text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.fine_slip_text.customContextMenuRequested.connect(self.show_fine_slip_context_menu)
        right_layout.addWidget(self.fine_slip_label)
        right_layout.addWidget(self.fine_slip_text)

        self.total_label = QLabel("总计")
        right_layout.addWidget(self.total_label)

        # 清除按钮
        self.clear_button = QPushButton("清除选中罪名")
        self.clear_button.clicked.connect(self.clear_selected_crimes)
        right_layout.addWidget(self.clear_button)

        right_widget.setLayout(right_layout)

        # 主窗口布局
        main_layout.addWidget(left_widget, 1)
        main_layout.addWidget(right_widget, 3)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.selected_crimes = []

    def on_law_item_clicked(self, item, column):
        law_data = item.data(column, Qt.UserRole)
        if law_data:
            self.description_box.setText(law_data["描述"])

            if law_data not in self.selected_crimes:
                self.selected_crimes.append(law_data)
                self.update_selected_crimes_table()

    def update_selected_crimes_table(self):
        self.selected_crimes_table.setRowCount(len(self.selected_crimes))
        for row, law_data in enumerate(self.selected_crimes):
            item_sin = QTableWidgetItem(law_data["罪名"])
            item_jail = QTableWidgetItem(str(law_data["监禁时长"])) if isinstance(law_data["监禁时长"], int) else QTableWidgetItem(law_data["监禁时长"])
            item_fine = QTableWidgetItem(str(law_data["罚款"])) if isinstance(law_data["罚款"], int) else QTableWidgetItem(law_data["罚款"])

            item_sin.setTextAlignment(Qt.AlignCenter)
            item_jail.setTextAlignment(Qt.AlignCenter)
            item_fine.setTextAlignment(Qt.AlignCenter)

            self.selected_crimes_table.setItem(row, 0, item_sin)
            self.selected_crimes_table.setItem(row, 1, item_jail)
            self.selected_crimes_table.setItem(row, 2, item_fine)

        self.update_fine_slip()

    def update_fine_slip(self):
        fine_slip_text = " ".join([law["罪名"] for law in self.selected_crimes] + ["罚款"])
        self.fine_slip_text.setText(fine_slip_text)

        total_crimes = len(self.selected_crimes)
        total_jail_time = 0
        total_fine = 0

        for law in self.selected_crimes:
            if isinstance(law["监禁时长"], int):
                total_jail_time += law["监禁时长"]
            if isinstance(law["罚款"], int):
                total_fine += law["罚款"]

        infinite_jail = any(law["监禁时长"] == "无限" for law in self.selected_crimes)
        if infinite_jail:
            total_jail_time = "无限"
            total_fine = "0"

        self.total_label.setText(f"总计：{total_crimes} 罪名，{total_jail_time} 分钟，{total_fine}$")

    def clear_selected_crimes(self):
        selected_rows = self.selected_crimes_table.selectedItems()
        if not selected_rows:
            return

        selected_row_indices = set(item.row() for item in selected_rows)

        for row in sorted(selected_row_indices, reverse=True):
            self.selected_crimes_table.removeRow(row)
            self.selected_crimes.pop(row)

        self.update_fine_slip()

    def show_fine_slip_context_menu(self, position):
        menu = QMenu(self.fine_slip_text)
        copy_action = menu.addAction("复制")
        copy_action.triggered.connect(lambda: self.copy_fine_slip_text())
        menu.exec_(self.fine_slip_text.mapToGlobal(position))

    def copy_fine_slip_text(self):
        text = self.fine_slip_text.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LawSystemApp()
    window.show()
    sys.exit(app.exec_())