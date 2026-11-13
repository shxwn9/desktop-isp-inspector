import base64
import socket
import threading
import time
import tkinter as tk
from tkinter import messagebox, ttk
import psutil

# [!] Obfuscated Author Signature & Brand Verification (Shawn / GIN / GINTTV)
_0x_sig_raw = b"RGVza3RvcCBJU1AgJiBOZXR3b3JrIEluc3BlY3RvciDigJQgYnkgU2hhd24gW0dJTl0gKFlUOiBHSU5UVFYp"
_0x_auth_raw = b"Q3JlYXRlZCBieSBTaGF3biB8IEdJTiB8IFlvdVR1YmU6IEdJTlRUVg=="
_0x_foot_raw = b"4pSBIFtHSU5dIERlc2t0b3AgVHJhZmZpYyBJbnNwZWN0b3IgfCBTaGF3biB8IFlvdVR1YmU6IEBHSU5UVFkg4pSB"

_0x_APP_TITLE = base64.b64decode(_0x_sig_raw).decode("utf-8")
_0x_DEV_CREDIT = base64.b64decode(_0x_auth_raw).decode("utf-8")
_0x_UI_FOOTER = base64.b64decode(_0x_foot_raw).decode("utf-8")

# Encoded port inspection profiles
_0x_MAP = {
    80: ("HTTP", "CRITICAL: Unencrypted (Full Content & URLs Visible)"),
    53: ("DNS", "CRITICAL: Plaintext Query (Domain Names Exposed)"),
    443: ("HTTPS", "METADATA: Domain & IPs Logged (SNI Handshake)"),
    853: ("DoT", "SECURE: Encrypted DNS"),
    9050: ("Tor SOCKS", "OBFUSCATED: Encrypted Tor Circuit"),
    9150: ("Tor Browser", "OBFUSCATED: Encrypted Tor Circuit"),
    5228: ("GCM/Firebase", "TELEMETRY: Google Push Service"),
    123: ("NTP", "TELEMETRY: Network Time Sync"),
    22: ("SSH", "ENCRYPTED: Secure Shell"),
}

_0x_CACHE = {}
_0x_QUEUE = set()


def _0x_dns_worker(ip):
    try:
        h = socket.gethostbyaddr(ip)[0]
    except Exception:
        h = "Unresolved / CDN Node"
    _0x_CACHE[ip] = h
    if ip in _0x_QUEUE:
        _0x_QUEUE.remove(ip)


class LocalTrafficInspector:

    def __init__(self, root):
        self.root = root

        # Enforce Anti-Tamper / Author Verification
        self._0x_verify_integrity()

        self.root.title(_0x_APP_TITLE)
        self.root.geometry("1100x650")

        self.last_io = psutil.net_io_counters()
        self.last_time = time.time()

        # Top Metric Frame
        top_frame = ttk.Frame(root, padding=10)
        top_frame.pack(fill=tk.X)

        self.lbl_bandwidth = ttk.Label(
            top_frame,
            text="Bandwidth: 0.0 KB/s DOWN | 0.0 KB/s UP",
            font=("Segoe UI", 10, "bold"),
        )
        self.lbl_bandwidth.pack(side=tk.LEFT)

        self.lbl_total_bytes = ttk.Label(
            top_frame, text="Total Monitored: 0 MB", font=("Segoe UI", 9)
        )
        self.lbl_total_bytes.pack(side=tk.RIGHT)

        # Search / Filter Bar
        search_frame = ttk.Frame(root, padding=(10, 0, 10, 8))
        search_frame.pack(fill=tk.X)

        ttk.Label(search_frame, text="Filter (App/IP):").pack(
            side=tk.LEFT, padx=(0, 5)
        )
        self.filter_var = tk.StringVar()
        self.entry_filter = ttk.Entry(
            search_frame, textvariable=self.filter_var, width=24
        )
        self.entry_filter.pack(side=tk.LEFT)

        self.lbl_active_conns = ttk.Label(
            search_frame, text="Active Sockets: 0", font=("Segoe UI", 9)
        )
        self.lbl_active_conns.pack(side=tk.RIGHT)

        # Main Telemetry Treeview
        columns = (
            "app",
            "pid",
            "remote_ip",
            "resolved_host",
            "port",
            "protocol",
            "isp_exposure",
        )
        self.tree = ttk.Treeview(
            root, columns=columns, show="headings", selectmode="browse"
        )

        self.tree.heading("app", text="Application")
        self.tree.heading("pid", text="PID")
        self.tree.heading("remote_ip", text="Destination IP")
        self.tree.heading(
            "resolved_host", text="Target Domain / Hostname (DPI Target)"
        )
        self.tree.heading("port", text="Port")
        self.tree.heading("protocol", text="Protocol")
        self.tree.heading("isp_exposure", text="ISP Exposure Status")

        self.tree.column("app", width=120)
        self.tree.column("pid", width=50, anchor=tk.CENTER)
        self.tree.column("remote_ip", width=140)
        self.tree.column("resolved_host", width=240)
        self.tree.column("port", width=60, anchor=tk.CENTER)
        self.tree.column("protocol", width=80, anchor=tk.CENTER)
        self.tree.column("isp_exposure", width=340)

        # Visual Severity Tags
        self.tree.tag_configure(
            "crit", background="#ffebee", foreground="#b71c1c"
        )
        self.tree.tag_configure(
            "meta", background="#fffde7", foreground="#e65100"
        )
        self.tree.tag_configure(
            "obfs", background="#e8f5e9", foreground="#1b5e20"
        )
        self.tree.tag_configure(
            "norm", background="#ffffff", foreground="#212121"
        )

        # Scrollbar
        sb = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=sb.set)

        self.tree.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(0, 5)
        )
        sb.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10))

        # Hardcoded Persistent Watermark Banner
        self.watermark_bar = tk.Label(
            root,
            text=_0x_UI_FOOTER,
            bg="#0f172a",
            fg="#38bdf8",
            font=("Segoe UI", 9, "bold"),
            pady=4,
        )
        self.watermark_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self._run_scan()

    def _0x_verify_integrity(self):
        """Enforces that the script cannot execute if Shawn / GIN credits are stripped."""
        _check_payload = [
            _0x_APP_TITLE,
            _0x_DEV_CREDIT,
            _0x_UI_FOOTER,
        ]
        if not all(
            any(k in s for k in ("Shawn", "GIN", "GINTTV"))
            for s in _check_payload
        ):
            print("[FATAL ERROR] Script integrity check failed. Unauthorized credit removal.")
            self.root.destroy()
            raise SystemExit(1)

    def _update_rates(self):
        now = time.time()
        cur_io = psutil.net_io_counters()
        dt = now - self.last_time

        if dt > 0:
            rx_rate = (cur_io.bytes_recv - self.last_io.bytes_recv) / dt
            tx_rate = (cur_io.bytes_sent - self.last_io.bytes_sent) / dt
            self.lbl_bandwidth.config(
                text=f"Bandwidth: {rx_rate/1024:.1f} KB/s DOWN | {tx_rate/1024:.1f} KB/s UP"
            )
            total_mb = (cur_io.bytes_recv + cur_io.bytes_sent) / (1024 * 1024)
            self.lbl_total_bytes.config(
                text=f"Total Monitored: {total_mb:.1f} MB"
            )

        self.last_io = cur_io
        self.last_time = now

    def _run_scan(self):
        self._update_rates()
        q = self.filter_var.get().strip().lower()
        rows = []

        try:
            for c in psutil.net_connections(kind="inet"):
                if c.raddr and c.status == "ESTABLISHED":
                    rip, rport, pid = c.raddr.ip, c.raddr.port, c.pid
                    if rip.startswith("127.") or rip == "::1":
                        continue

                    pname = "System Protected"
                    if pid:
                        try:
                            pname = psutil.Process(pid).name()
                        except Exception:
                            pass

                    # Resolve PTR domain
                    if rip in _0x_CACHE:
                        host = _0x_CACHE[rip]
                    else:
                        host = "Resolving..."
                        if rip not in _0x_QUEUE:
                            _0x_QUEUE.add(rip)
                            threading.Thread(
                                target=_0x_dns_worker, args=(rip,), daemon=True
                            ).start()

                    p_proto, p_desc = _0x_MAP.get(
                        rport, ("TCP", "METADATA: Remote Socket Active")
                    )

                    tag = "norm"
                    if rport in (80, 53):
                        tag = "crit"
                    elif rport == 443:
                        tag = "meta"
                    elif rport in (9050, 9150):
                        tag = "obfs"

                    if q and q not in f"{pname} {rip} {host} {p_proto}".lower():
                        continue

                    rows.append(
                        (
                            pname,
                            pid or "-",
                            rip,
                            host,
                            rport,
                            p_proto,
                            p_desc,
                            tag,
                        )
                    )
        except Exception:
            pass

        self.tree.delete(*self.tree.get_children())
        for r in rows:
            self.tree.insert("", tk.END, values=r[:-1], tags=(r[-1],))

        self.lbl_active_conns.config(text=f"Active Sockets: {len(rows)}")
        self.root.after(2000, self._run_scan)


if __name__ == "__main__":
    print(
        f"\n======================================================\n"
        f" [*] {_0x_APP_TITLE}\n"
        f" [*] {_0x_DEV_CREDIT}\n"
        f"======================================================\n"
    )
    root = tk.Tk()
    app = LocalTrafficInspector(root)
    root.mainloop()