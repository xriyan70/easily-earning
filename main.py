from flask import Flask, render_template_string, request

app = Flask(__name__)

# এডমিন কন্ট্রোল প্যানেলের তথ্য
config = {
    "refer_bonus": 5,      # প্রতি রেফারে ৫ টাকা
    "commission": 5,       # ৫% কমিশন
    "admin_pass": "maruf786",
    "tg_link": "#",
    "fb_link": "#"
}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Easily Earning Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root { --primary: #77e621; --nagad: #ed1c24; --bg: #f8fafc; --text: #1e293b; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--bg); color: var(--text); padding-bottom: 100px; }
        
        .top-nav { background: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 100; }
        .coins-box { background: #f1f5f9; padding: 6px 15px; border-radius: 20px; font-weight: 700; color: #b45309; font-size: 14px; }

        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* Referral Earnings Card (Image 10) */
        .refer-stat-card { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-around; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .stat-item b { font-size: 20px; display: block; color: #000; }
        .stat-item span { font-size: 11px; color: #64748b; font-weight: 600; }

        /* Leaderboard Podiums (Image 12 style) */
        .podium-container { display: flex; justify-content: center; align-items: flex-end; gap: 15px; margin: 30px 0; }
        .podium { background: #fff; width: 95px; border-radius: 20px; padding: 15px 5px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); position: relative; }
        .p-1 { height: 150px; border-top: 5px solid #fbbf24; transform: scale(1.1); z-index: 2; }
        .p-2 { height: 120px; border-top: 5px solid #cbd5e1; }
        .p-3 { height: 100px; border-top: 5px solid #cd7f32; }
        .gmail-img { width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 700; font-size: 20px; margin: 0 auto 10px; border: 3px solid #fff; }

        /* Withdraw List Box (As requested) */
        .payout-box { background: #fff; border-radius: 20px; padding: 15px; margin-top: 20px; border: 1px solid #e2e8f0; }
        .payout-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px dashed #e2e8f0; font-size: 12px; }
        .payout-item:last-child { border: none; }

        /* Withdraw Cards (Image 14 style) */
        .w-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .history-btn { color: #64748b; font-size: 14px; text-decoration: none; font-weight: 600; }
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        .w-card { background: #fff; border-radius: 20px; padding: 20px; text-align: center; border: 2px solid transparent; transition: 0.3s; cursor: pointer; }
        .w-card img { width: 60px; margin-bottom: 10px; }
        .w-card h4 { margin: 5px 0; font-size: 22px; }
        .w-card.selected { border-color: var(--nagad); background: #fff5f5; }

        .refer-btn { position: fixed; bottom: 85px; left: 5%; width: 90%; background: var(--primary); color: #000; border: none; padding: 18px; border-radius: 40px; font-weight: 800; font-size: 18px; box-shadow: 0 5px 20px rgba(119,230,33,0.3); z-index: 100; }

        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #e2e8f0; }
        .nav-item { text-align: center; color: #94a3b8; font-size: 10px; font-weight: 700; cursor: pointer; text-decoration: none; }
        .nav-item i { font-size: 22px; display: block; margin-bottom: 4px; }
        .active-nav { color: var(--primary); }
    </style>
</head>
<body>

    <div class="top-nav">
        <b style="font-size: 18px;">EASILY EARNING</b>
        <div class="coins-box"><i class="fas fa-coins"></i> 81,480 ≈ ৳81.48</div>
    </div>

    <div id="home" class="page active">
        <h3 style="margin-bottom: 15px;">Available Tasks</h3>
        <div style="background:#fff; padding:20px; border-radius:20px; display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <div><b>Video Task 01</b><br><small style="color:var(--primary); font-weight:700;">Reward: ৳15.00</small></div>
            <button style="background:var(--primary); border:none; padding:8px 20px; border-radius:15px; font-weight:700;" onclick="showPage('tasks', 1)">Earn</button>
        </div>
        </div>

    <div id="refer" class="page" style="padding-bottom:150px;">
        <div class="refer-stat-card">
            <div class="stat-item"><b>0</b><span>Commission</span></div>
            <div class="stat-item"><b>0 <i class="far fa-question-circle" style="color:orange; font-size:10px;"></i></b><span>Pending</span></div>
            <div class="stat-item"><b>0</b><span>Referrals</span></div>
        </div>

        <div class="podium-container">
            <div class="podium p-2"><div class="gmail-img" style="background:#4caf50;">P</div><b>Pujan</b><br><small>৳4,200</small></div>
            <div class="podium p-1"><i class="fas fa-crown" style="position:absolute; top:-20px; left:38%; color:#fbbf24;"></i><div class="gmail-img" style="background:#f44336;">M</div><b>Maruf</b><br><small>৳5,800</small></div>
            <div class="podium p-3"><div class="gmail-img" style="background:#2196f3;">S</div><b>Sohag</b><br><small>৳3,500</small></div>
        </div>

        <div style="background:white; padding:20px; border-radius:20px; text-align:center;">
            <p style="font-size:13px; font-weight:600;">Refer a friend and get ৳5.00 + 5% Commission!</p>
            <div style="display:flex; justify-content:center; gap:20px; margin-top:15px;">
                <i class="fab fa-facebook" style="font-size:30px; color:#1877f2;"></i>
                <i class="fab fa-telegram" style="font-size:30px; color:#229ed9;"></i>
                <i class="fas fa-copy" style="font-size:30px; color:#64748b;"></i>
            </div>
        </div>

        <button class="refer-btn" onclick="alert('Link Copied!')">Refer now</button>
    </div>

    <div id="withdraw" class="page">
        <div class="w-header">
            <b style="font-size: 20px;">Withdrawable</b>
            <a href="#" class="history-btn" onclick="alert('Loading History...')">History <i class="fas fa-chevron-right" style="font-size:10px;"></i></a>
        </div>

        <div class="w-grid">
            <div class="w-card" onclick="sel(this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳100</h4>
                <small style="color:#64748b;">100,000 Coins</small>
            </div>
            <div class="w-card" onclick="sel(this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳200</h4>
                <small style="color:#64748b;">200,000 Coins</small>
            </div>
            <div class="w-card" onclick="sel(this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳300</h4>
                <small style="color:#64748b;">300,000 Coins</small>
            </div>
            <div class="w-card" onclick="sel(this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳500</h4>
                <small style="color:#64748b;">500,000 Coins</small>
            </div>
        </div>

        <div class="payout-box">
            <h5 style="margin:0 0 10px 0; color:var(--nagad);"><i class="fas fa-bolt"></i> Live Payouts</h5>
            <div id="live-list">
                </div>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item active-nav" onclick="showPage('home', this)"><i class="fas fa-gift"></i>Offer</div>
        <div class="nav-item" onclick="showPage('tasks', this)"><i class="fas fa-clipboard-list"></i>My offers</div>
        <div class="nav-item" onclick="showPage('refer', this)"><i class="fas fa-user-plus"></i>Refer</div>
        <div class="nav-item" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i>Cashout</div>
    </div>

    <script>
        function showPage(id, el) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active-nav'));
            if(el) el.classList.add('active-nav');
        }

        function sel(el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
        }

        // Live Withdraw List
        const names = ["Maruf", "Pujan", "Siyam", "Abir", "Mursalin", "Rifat", "Sumon"];
        function updateLive() {
            const list = document.getElementById('live-list');
            const name = names[Math.floor(Math.random() * names.length)];
            const amt = [100, 200, 500][Math.floor(Math.random() * 3)];
            const item = `<div class="payout-item"><span>${name} [Nagad]</span> <b style="color:green;">+ ৳${amt}</b></div>`;
            list.innerHTML = item + list.innerHTML;
            if(list.children.length > 5) list.lastElementChild.remove();
        }
        setInterval(updateLive, 6000);
        updateLive();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
