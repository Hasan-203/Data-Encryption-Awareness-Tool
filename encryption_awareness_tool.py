import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet


# ============================================================
# Data Encryption Awareness Tool
# Educational cybersecurity awareness application
# ============================================================

class EncryptionAwarenessTool:
    BG = "#071426"
    SIDEBAR = "#06101f"
    PANEL = "#0c1d32"
    PANEL_2 = "#102640"
    BORDER = "#1d3a5c"
    TEXT = "#f4f7fb"
    MUTED = "#aab8c8"
    BLUE = "#2396ff"
    GREEN = "#38d77a"
    PURPLE = "#a66cff"
    ORANGE = "#ff9f43"
    RED = "#ff5c70"

    def __init__(self, root):
        self.root = root
        self.root.title("Data Encryption Awareness Tool")
        self.root.geometry("1200x760")
        self.root.minsize(1050, 680)
        self.root.configure(bg=self.BG)

        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.last_encrypted = ""

        self.pages = {}
        self.nav_buttons = {}

        self.build_layout()
        self.show_page("Awareness")

    # -------------------- Layout --------------------

    def build_layout(self):
        self.sidebar = tk.Frame(self.root, bg=self.SIDEBAR, width=245)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.content = tk.Frame(self.root, bg=self.BG)
        self.content.pack(side="right", fill="both", expand=True)

        self.build_sidebar()

        self.pages["Awareness"] = self.create_scrollable_page()
        self.pages["Encryption Demo"] = self.create_scrollable_page()
        self.pages["Security Tips"] = self.create_scrollable_page()
        self.pages["Quiz"] = self.create_scrollable_page()
        self.pages["About"] = self.create_scrollable_page()

        self.build_awareness()
        self.build_demo()
        self.build_tips()
        self.build_quiz()
        self.build_about()

    def build_sidebar(self):
        logo_area = tk.Frame(self.sidebar, bg=self.SIDEBAR)
        logo_area.pack(fill="x", pady=(28, 25))

        tk.Label(
            logo_area,
            text="🔐",
            font=("Segoe UI Emoji", 42),
            bg=self.SIDEBAR,
            fg=self.BLUE
        ).pack()

        tk.Label(
            logo_area,
            text="DATA ENCRYPTION",
            font=("Segoe UI", 15, "bold"),
            bg=self.SIDEBAR,
            fg=self.TEXT
        ).pack()

        tk.Label(
            logo_area,
            text="AWARENESS TOOL",
            font=("Segoe UI", 12, "bold"),
            bg=self.SIDEBAR,
            fg=self.BLUE
        ).pack(pady=(2, 0))

        tk.Frame(self.sidebar, bg=self.BORDER, height=1).pack(fill="x", padx=18, pady=(0, 18))

        items = [
            ("⌂", "Awareness"),
            ("🔒", "Encryption Demo"),
            ("🛡", "Security Tips"),
            ("☑", "Quiz"),
            ("ⓘ", "About"),
        ]

        for icon, name in items:
            btn = tk.Button(
                self.sidebar,
                text=f"  {icon}   {name}",
                command=lambda n=name: self.show_page(n),
                anchor="w",
                font=("Segoe UI", 11),
                bg=self.SIDEBAR,
                fg=self.MUTED,
                activebackground="#12345b",
                activeforeground=self.TEXT,
                relief="flat",
                bd=0,
                padx=18,
                pady=13,
                cursor="hand2"
            )
            btn.pack(fill="x", padx=12, pady=3)
            self.nav_buttons[name] = btn

        spacer = tk.Frame(self.sidebar, bg=self.SIDEBAR)
        spacer.pack(fill="both", expand=True)

        quote = tk.Frame(
            self.sidebar,
            bg="#0a1a2d",
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        quote.pack(fill="x", padx=18, pady=18)

        tk.Label(
            quote,
            text="“",
            font=("Georgia", 28, "bold"),
            bg="#0a1a2d",
            fg=self.BLUE
        ).pack(anchor="w", padx=12, pady=(5, 0))

        tk.Label(
            quote,
            text="Encryption is not about\nhiding information.\nIt is about protecting\nwhat matters.",
            font=("Segoe UI", 9),
            justify="center",
            bg="#0a1a2d",
            fg=self.MUTED
        ).pack(padx=8, pady=(0, 8))

        tk.Label(
            self.sidebar,
            text="Stay Safe. Stay Encrypted. 🔒",
            font=("Segoe UI", 9),
            bg=self.SIDEBAR,
            fg=self.MUTED
        ).pack(pady=(0, 20))

    def create_scrollable_page(self):
        outer = tk.Frame(self.content, bg=self.BG)

        canvas = tk.Canvas(
            outer,
            bg=self.BG,
            highlightthickness=0,
            bd=0
        )
        scrollbar = tk.Scrollbar(
            outer,
            orient="vertical",
            command=canvas.yview
        )

        inner = tk.Frame(canvas, bg=self.BG)
        inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        window_id = canvas.create_window(
            (0, 0),
            window=inner,
            anchor="nw"
        )

        def resize_inner(event):
            canvas.itemconfig(window_id, width=event.width)

        canvas.bind("<Configure>", resize_inner)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        outer.inner = inner
        return outer

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(fill="both", expand=True)

        for name, btn in self.nav_buttons.items():
            if name == page_name:
                btn.configure(
                    bg="#12345b",
                    fg=self.TEXT,
                    font=("Segoe UI", 11, "bold")
                )
            else:
                btn.configure(
                    bg=self.SIDEBAR,
                    fg=self.MUTED,
                    font=("Segoe UI", 11)
                )

        # Return to the top when changing pages.
        canvas = self.pages[page_name].winfo_children()[0]
        canvas.yview_moveto(0)

    # -------------------- Helpers --------------------

    def title(self, parent, text, subtitle=None):
        frame = tk.Frame(parent, bg=self.BG)
        frame.pack(fill="x", padx=35, pady=(28, 15))

        tk.Label(
            frame,
            text=text,
            font=("Segoe UI", 26, "bold"),
            bg=self.BG,
            fg=self.TEXT
        ).pack(anchor="w")

        if subtitle:
            tk.Label(
                frame,
                text=subtitle,
                font=("Segoe UI", 11),
                bg=self.BG,
                fg=self.MUTED
            ).pack(anchor="w", pady=(5, 0))

        return frame

    def card(self, parent, title, text, accent, width=300):
        frame = tk.Frame(
            parent,
            bg=self.PANEL,
            highlightbackground=accent,
            highlightthickness=1,
            bd=0
        )

        tk.Frame(frame, bg=accent, height=4).pack(fill="x")

        body = tk.Frame(frame, bg=self.PANEL)
        body.pack(fill="both", expand=True, padx=18, pady=15)

        tk.Label(
            body,
            text=title,
            font=("Segoe UI", 14, "bold"),
            bg=self.PANEL,
            fg=accent
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            body,
            text=text,
            font=("Segoe UI", 10),
            justify="left",
            wraplength=width - 45,
            bg=self.PANEL,
            fg=self.MUTED
        ).pack(anchor="w")

        return frame

    def section(self, parent, text):
        tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 17, "bold"),
            bg=self.BG,
            fg=self.TEXT
        ).pack(anchor="w", padx=35, pady=(20, 12))

    # -------------------- Awareness --------------------

    def build_awareness(self):
        page = self.pages["Awareness"].inner

        self.title(
            page,
            "🔐  Data Encryption Awareness",
            "Learn • Encrypt • Protect"
        )

        hero = tk.Frame(
            page,
            bg=self.PANEL,
            highlightbackground=self.BLUE,
            highlightthickness=1
        )
        hero.pack(fill="x", padx=35, pady=5)

        left = tk.Frame(hero, bg=self.PANEL)
        left.pack(side="left", fill="both", expand=True, padx=25, pady=24)

        tk.Label(
            left,
            text="Protecting your digital information",
            font=("Segoe UI", 18, "bold"),
            bg=self.PANEL,
            fg=self.TEXT
        ).pack(anchor="w")

        tk.Label(
            left,
            text=(
                "Encryption converts readable information (plaintext) into "
                "an unreadable format (ciphertext). The correct key allows "
                "an authorized user to recover the original information."
            ),
            font=("Segoe UI", 11),
            justify="left",
            wraplength=700,
            bg=self.PANEL,
            fg=self.MUTED
        ).pack(anchor="w", pady=(10, 0))

        tk.Label(
            hero,
            text="🔒",
            font=("Segoe UI Emoji", 58),
            bg=self.PANEL,
            fg=self.BLUE
        ).pack(side="right", padx=40)

        # Three information cards
        cards = tk.Frame(page, bg=self.BG)
        cards.pack(fill="x", padx=35, pady=20)

        data = [
            (
                "🔒  Confidentiality",
                "Encryption helps keep sensitive information private and prevents unauthorized people from reading it.",
                self.BLUE
            ),
            (
                "✓  Integrity",
                "Encrypted systems can help protect information while it is stored or transferred.",
                self.GREEN
            ),
            (
                "👤  Authentication",
                "Secure systems use keys and identity controls to ensure data is accessed by authorized users.",
                self.PURPLE
            ),
        ]

        for i, (t, txt, color) in enumerate(data):
            c = self.card(cards, t, txt, color, 330)
            c.grid(row=0, column=i, padx=6, sticky="nsew")
            cards.grid_columnconfigure(i, weight=1)

        # How it works
        self.section(page, "How Encryption Works")

        workflow = tk.Frame(
            page,
            bg=self.PANEL,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        workflow.pack(fill="x", padx=35, pady=(0, 18))

        steps = [
            ("Original Message", "Hello World!", self.BLUE),
            ("Encryption", "🔒 Using a Key", self.GREEN),
            ("Ciphertext", "gAAAAAB...\nXk9QmJ2...", self.PURPLE),
            ("Decryption", "🔓 Using the Key", self.ORANGE),
            ("Original Message", "Hello World!", self.BLUE),
        ]

        for i, (heading, value, color) in enumerate(steps):
            box = tk.Frame(
                workflow,
                bg="#0a1a2d",
                highlightbackground=color,
                highlightthickness=1
            )
            box.grid(row=0, column=i, padx=8, pady=18, sticky="nsew")
            workflow.grid_columnconfigure(i, weight=1)

            tk.Label(
                box,
                text=heading,
                font=("Segoe UI", 9, "bold"),
                bg="#0a1a2d",
                fg=color
            ).pack(pady=(12, 8))

            tk.Label(
                box,
                text=value,
                font=("Consolas", 10),
                justify="center",
                bg="#0a1a2d",
                fg=self.TEXT
            ).pack(padx=8, pady=(0, 12))

            if i < len(steps) - 1:
                tk.Label(
                    workflow,
                    text="→",
                    font=("Segoe UI", 18, "bold"),
                    bg=self.PANEL,
                    fg=self.MUTED
                ).grid(row=0, column=i, sticky="e", padx=(0, 2))

        note = tk.Frame(
            workflow,
            bg="#102640"
        )
        note.grid(row=1, column=0, columnspan=5, sticky="ew", padx=18, pady=(0, 18))

        tk.Label(
            note,
            text="💡  Without the correct key, encrypted data cannot be easily understood.",
            font=("Segoe UI", 10, "bold"),
            bg="#102640",
            fg=self.TEXT
        ).pack(pady=10)

        # Why it matters
        bottom = tk.Frame(page, bg=self.BG)
        bottom.pack(fill="x", padx=35, pady=(0, 25))

        why = tk.Frame(
            bottom,
            bg=self.PANEL,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        why.pack(side="left", fill="both", expand=True, padx=(0, 8))

        tk.Label(
            why,
            text="Why It Matters?",
            font=("Segoe UI", 16, "bold"),
            bg=self.PANEL,
            fg=self.TEXT
        ).pack(anchor="w", padx=20, pady=(16, 10))

        reasons = [
            "🔐 Protects personal data from attackers",
            "💳 Secures sensitive online transactions",
            "☁ Protects information stored in the cloud",
            "✉ Helps protect data during communication",
            "🛡 Reduces the impact of unauthorized access"
        ]

        for reason in reasons:
            tk.Label(
                why,
                text=reason,
                font=("Segoe UI", 10),
                bg=self.PANEL,
                fg=self.MUTED,
                anchor="w"
            ).pack(fill="x", padx=20, pady=5)

        why.pack_propagate(False)

        action = tk.Frame(
            bottom,
            bg="#0b2139",
            highlightbackground=self.BLUE,
            highlightthickness=1
        )
        action.pack(side="right", fill="both", padx=(8, 0))

        tk.Label(
            action,
            text="🚀  Try it yourself!",
            font=("Segoe UI", 16, "bold"),
            bg="#0b2139",
            fg=self.TEXT
        ).pack(pady=(20, 8))

        tk.Label(
            action,
            text="Encrypt a real message and\nsee how the data changes.",
            font=("Segoe UI", 10),
            justify="center",
            bg="#0b2139",
            fg=self.MUTED
        ).pack()

        tk.Button(
            action,
            text="Go to Encryption Demo  →",
            command=lambda: self.show_page("Encryption Demo"),
            bg=self.BLUE,
            fg="white",
            activebackground="#1684e5",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            padx=18,
            pady=9,
            cursor="hand2"
        ).pack(pady=18)

    # -------------------- Encryption Demo --------------------

    def build_demo(self):
        page = self.pages["Encryption Demo"].inner

        self.title(
            page,
            "🔐  Live Encryption Demo",
            "Experience symmetric encryption step by step"
        )

        info = tk.Frame(
            page,
            bg="#0b2139",
            highlightbackground=self.BLUE,
            highlightthickness=1
        )
        info.pack(fill="x", padx=35, pady=(0, 18))

        tk.Label(
            info,
            text=(
                "This educational demo uses Fernet symmetric encryption. "
                "The same secret key is used for encryption and decryption."
            ),
            font=("Segoe UI", 10),
            bg="#0b2139",
            fg=self.MUTED,
            wraplength=900
        ).pack(anchor="w", padx=18, pady=13)

        # Input card
        input_card = tk.Frame(
            page,
            bg=self.PANEL,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        input_card.pack(fill="x", padx=35, pady=8)

        tk.Label(
            input_card,
            text="1. Enter your message",
            font=("Segoe UI", 14, "bold"),
            bg=self.PANEL,
            fg=self.TEXT
        ).pack(anchor="w", padx=18, pady=(15, 8))

        self.message_box = tk.Text(
            input_card,
            height=5,
            font=("Segoe UI", 11),
            bg="#08182b",
            fg=self.TEXT,
            insertbackground=self.TEXT,
            relief="flat",
            padx=12,
            pady=10,
            wrap="word"
        )
        self.message_box.pack(fill="x", padx=18, pady=(0, 14))

        buttons = tk.Frame(input_card, bg=self.PANEL)
        buttons.pack(fill="x", padx=18, pady=(0, 16))

        self.make_button(
            buttons,
            "🔐  Encrypt Message",
            self.encrypt_message,
            self.BLUE
        ).pack(side="left", padx=(0, 8))

        self.make_button(
            buttons,
            "Clear",
            self.clear_demo,
            "#263b53"
        ).pack(side="left")

        # Encrypted output
        output_card = tk.Frame(
            page,
            bg=self.PANEL,
            highlightbackground=self.PURPLE,
            highlightthickness=1
        )
        output_card.pack(fill="x", padx=35, pady=8)

        tk.Label(
            output_card,
            text="2. Encrypted Data (Ciphertext)",
            font=("Segoe UI", 14, "bold"),
            bg=self.PANEL,
            fg=self.PURPLE
        ).pack(anchor="w", padx=18, pady=(15, 8))

        self.encrypted_box = tk.Text(
            output_card,
            height=6,
            font=("Consolas", 10),
            bg="#08182b",
            fg="#d8c7ff",
            insertbackground=self.TEXT,
            relief="flat",
            padx=12,
            pady=10,
            wrap="word"
        )
        self.encrypted_box.pack(fill="x", padx=18, pady=(0, 14))

        # Decryption
        decrypt_card = tk.Frame(
            page,
            bg=self.PANEL,
            highlightbackground=self.GREEN,
            highlightthickness=1
        )
        decrypt_card.pack(fill="x", padx=35, pady=8)

        tk.Label(
            decrypt_card,
            text="3. Decrypt the data",
            font=("Segoe UI", 14, "bold"),
            bg=self.PANEL,
            fg=self.GREEN
        ).pack(anchor="w", padx=18, pady=(15, 8))

        self.decrypted_box = tk.Text(
            decrypt_card,
            height=4,
            font=("Segoe UI", 11),
            bg="#08182b",
            fg="#c8ffd9",
            insertbackground=self.TEXT,
            relief="flat",
            padx=12,
            pady=10,
            wrap="word"
        )
        self.decrypted_box.pack(fill="x", padx=18, pady=(0, 14))

        self.make_button(
            decrypt_card,
            "🔓  Decrypt Message",
            self.decrypt_message,
            self.GREEN,
            fg="#03150a"
        ).pack(anchor="w", padx=18, pady=(0, 18))

        tk.Label(
            page,
            text="Educational use only • Do not enter real passwords or confidential information.",
            font=("Segoe UI", 9),
            bg=self.BG,
            fg=self.MUTED
        ).pack(pady=15)

    def make_button(self, parent, text, command, bg, fg="white"):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            padx=16,
            pady=9,
            cursor="hand2"
        )

    def encrypt_message(self):
        message = self.message_box.get("1.0", "end").strip()

        if not message:
            messagebox.showwarning(
                "Empty Message",
                "Please enter a message first."
            )
            return

        self.last_encrypted = self.cipher.encrypt(
            message.encode("utf-8")
        ).decode("utf-8")

        self.encrypted_box.delete("1.0", "end")
        self.encrypted_box.insert("1.0", self.last_encrypted)

        self.decrypted_box.delete("1.0", "end")

    def decrypt_message(self):
        encrypted = self.encrypted_box.get("1.0", "end").strip()

        if not encrypted:
            messagebox.showwarning(
                "No Ciphertext",
                "Encrypt a message first."
            )
            return

        try:
            decrypted = self.cipher.decrypt(
                encrypted.encode("utf-8")
            ).decode("utf-8")

            self.decrypted_box.delete("1.0", "end")
            self.decrypted_box.insert("1.0", decrypted)

        except Exception:
            messagebox.showerror(
                "Decryption Error",
                "The encrypted data is invalid or the key does not match."
            )

    def clear_demo(self):
        for box in [self.message_box, self.encrypted_box, self.decrypted_box]:
            box.delete("1.0", "end")

    # -------------------- Security Tips --------------------

    def build_tips(self):
        page = self.pages["Security Tips"].inner

        self.title(
            page,
            "🛡  Cybersecurity Security Tips",
            "Small security habits can make a big difference"
        )

        tips = [
            (
                "01",
                "Protect Sensitive Data",
                "Use encryption to protect personal, financial, academic, and business information.",
                self.BLUE
            ),
            (
                "02",
                "Use Strong Passwords",
                "Create long, unique passwords and avoid reusing the same password across websites.",
                self.GREEN
            ),
            (
                "03",
                "Enable MFA",
                "Multi-Factor Authentication adds an additional security layer if your password is compromised.",
                self.PURPLE
            ),
            (
                "04",
                "Be Careful With Phishing",
                "Check links, senders, and unexpected requests before providing credentials or sensitive data.",
                self.ORANGE
            ),
            (
                "05",
                "Keep Software Updated",
                "Security updates often fix vulnerabilities that attackers could use to compromise systems.",
                self.BLUE
            ),
            (
                "06",
                "Use Secure Connections",
                "Prefer HTTPS and trusted networks when transmitting sensitive information.",
                self.GREEN
            ),
        ]

        grid = tk.Frame(page, bg=self.BG)
        grid.pack(fill="x", padx=35, pady=5)

        for i, (number, title, text, color) in enumerate(tips):
            card = tk.Frame(
                grid,
                bg=self.PANEL,
                highlightbackground=self.BORDER,
                highlightthickness=1
            )
            card.grid(
                row=i // 2,
                column=i % 2,
                padx=7,
                pady=7,
                sticky="nsew"
            )

            grid.grid_columnconfigure(0, weight=1)
            grid.grid_columnconfigure(1, weight=1)

            tk.Label(
                card,
                text=number,
                font=("Segoe UI", 18, "bold"),
                bg=self.PANEL,
                fg=color
            ).pack(anchor="w", padx=18, pady=(15, 3))

            tk.Label(
                card,
                text=title,
                font=("Segoe UI", 13, "bold"),
                bg=self.PANEL,
                fg=self.TEXT
            ).pack(anchor="w", padx=18)

            tk.Label(
                card,
                text=text,
                font=("Segoe UI", 10),
                bg=self.PANEL,
                fg=self.MUTED,
                wraplength=430,
                justify="left"
            ).pack(anchor="w", padx=18, pady=(7, 17))

    # -------------------- Quiz --------------------

    def build_quiz(self):
        page = self.pages["Quiz"].inner

        self.title(
            page,
            "🎯  Encryption Awareness Quiz",
            "Test what you learned"
        )

        self.quiz_questions = [
            (
                "What is the main purpose of encryption?",
                [
                    "Make data public",
                    "Protect data from unauthorized access",
                    "Delete data",
                    "Increase internet speed"
                ],
                1
            ),
            (
                "What is plaintext?",
                [
                    "Encrypted data",
                    "Readable original data",
                    "A firewall",
                    "A password manager"
                ],
                1
            ),
            (
                "What is ciphertext?",
                [
                    "Readable data",
                    "A network cable",
                    "Encrypted or transformed data",
                    "A username"
                ],
                2
            ),
            (
                "Which action improves account security?",
                [
                    "Reuse one password everywhere",
                    "Disable updates",
                    "Enable Multi-Factor Authentication",
                    "Share your password"
                ],
                2
            ),
        ]

        self.quiz_vars = []

        for i, (question, options, correct) in enumerate(self.quiz_questions):
            card = tk.Frame(
                page,
                bg=self.PANEL,
                highlightbackground=self.BORDER,
                highlightthickness=1
            )
            card.pack(fill="x", padx=35, pady=6)

            tk.Label(
                card,
                text=f"{i + 1}.  {question}",
                font=("Segoe UI", 11, "bold"),
                bg=self.PANEL,
                fg=self.TEXT,
                wraplength=850,
                justify="left"
            ).pack(anchor="w", padx=18, pady=(14, 8))

            var = tk.IntVar(value=-1)
            self.quiz_vars.append(var)

            for j, option in enumerate(options):
                tk.Radiobutton(
                    card,
                    text=option,
                    variable=var,
                    value=j,
                    font=("Segoe UI", 10),
                    bg=self.PANEL,
                    fg=self.MUTED,
                    selectcolor="#163454",
                    activebackground=self.PANEL,
                    activeforeground=self.TEXT
                ).pack(anchor="w", padx=35, pady=2)

            tk.Frame(card, bg=self.PANEL, height=10).pack()

        self.make_button(
            page,
            "✓  Check My Answers",
            self.check_quiz,
            self.BLUE
        ).pack(anchor="w", padx=35, pady=15)

        self.quiz_result = tk.Label(
            page,
            text="",
            font=("Segoe UI", 12, "bold"),
            bg=self.BG,
            fg=self.GREEN
        )
        self.quiz_result.pack(anchor="w", padx=35, pady=(0, 25))

    def check_quiz(self):
        score = 0
        unanswered = 0

        for var, (_, _, correct) in zip(
            self.quiz_vars,
            self.quiz_questions
        ):
            answer = var.get()

            if answer == -1:
                unanswered += 1
            elif answer == correct:
                score += 1

        if unanswered:
            self.quiz_result.configure(
                text=f"Please answer all questions. Unanswered: {unanswered}",
                fg=self.ORANGE
            )
            return

        total = len(self.quiz_questions)

        if score == total:
            result = f"Excellent! {score}/{total}  🎉"
            color = self.GREEN
        elif score >= 3:
            result = f"Good job! {score}/{total}  👍"
            color = self.BLUE
        else:
            result = f"You scored {score}/{total}. Review the Security Tips and try again."
            color = self.ORANGE

        self.quiz_result.configure(text=result, fg=color)

    # -------------------- About --------------------

    def build_about(self):
        page = self.pages["About"].inner

        self.title(
            page,
            "ⓘ  About This Project",
            "Data Encryption Awareness Tool"
        )

        about = tk.Frame(
            page,
            bg=self.PANEL,
            highlightbackground=self.BLUE,
            highlightthickness=1
        )
        about.pack(fill="x", padx=35, pady=10)

        tk.Label(
            about,
            text="Project Overview",
            font=("Segoe UI", 18, "bold"),
            bg=self.PANEL,
            fg=self.TEXT
        ).pack(anchor="w", padx=22, pady=(20, 10))

        text = (
            "The Data Encryption Awareness Tool is an interactive cybersecurity "
            "education project designed to explain the importance of encryption "
            "and demonstrate how encrypted data can be protected from unauthorized access.\n\n"
            "The project provides a live encryption/decryption demonstration, "
            "security awareness tips, and a short quiz to reinforce learning.\n\n"
            "Technology: Python • Tkinter • Cryptography (Fernet)"
        )

        tk.Label(
            about,
            text=text,
            font=("Segoe UI", 11),
            justify="left",
            wraplength=900,
            bg=self.PANEL,
            fg=self.MUTED
        ).pack(anchor="w", padx=22, pady=(0, 22))

        credit = tk.Frame(
            page,
            bg="#0b2139",
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        credit.pack(fill="x", padx=35, pady=10)

        tk.Label(
            credit,
            text="Presented at Nabeh 2024",
            font=("Segoe UI", 16, "bold"),
            bg="#0b2139",
            fg=self.BLUE
        ).pack(pady=(20, 5))

        tk.Label(
            credit,
            text="An educational project focused on improving cybersecurity awareness and understanding of data encryption.",
            font=("Segoe UI", 10),
            bg="#0b2139",
            fg=self.MUTED,
            wraplength=850,
            justify="center"
        ).pack(pady=(0, 20))


if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionAwarenessTool(root)
    root.mainloop()
