from flask import Flask, render_template_string

app = Flask(__name__)

# এই config সেকশন থেকে আপনি ওয়েবসাইট কন্ট্রোল করতে পারবেন
config = {
    "task_name": "Watch & Subscribe - 01",
    "refer_bonus": 5,      # প্রতি রেফারে ৫ টাকা
    "commission": 5,       # ৫% লাইফটাইম কমিশন
    "admin_pass": "maruf786"
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
        body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--bg); color: var(--text); padding-bottom: 110px; }
        
        /* Navigation */
        .top-nav { background: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 100; }
        .coins-box { background: #f1f5f9; padding: 6px 15px; border-radius: 20px; font-weight: 700; color: #b45309; font-size: 14px; }

        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* Referral Dashboard (Image 22610 style) */
        .refer-dashboard { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-around; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .stat-box b { font-size: 18px; display: block; color: #000; }
        .stat-box span { font-size: 11px; color: #64748b; font-weight: 600; }

        /* Leaderboard (Image 22612 style) */
        .podium-container { display: flex; justify-content: center; align-items: flex-end; gap: 12px; margin: 35px 0 20px; }
        .podium { background: #fff; width: 95px; border-radius: 20px; padding: 15px 5px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); position: relative; }
        .p-1 { height: 145px; border-top: 5px solid #fbbf24; transform: scale(1.1); z-index: 2; }
        .p-2 { height: 115px; border-top: 5px solid #cbd5e1; }
        .p-3 { height: 95px; border-top: 5px solid #cd7f32; }
        .gmail-img { width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 700; margin: 0 auto 10px; border: 2px solid #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }

        /* User List Box */
        .user-list { background: #fff; border-radius: 20px; padding: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.02); }
        .user-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #f1f5f9; }

        /* Withdraw Section (Image 22614 style) */
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
        .w-card { background: #fff; border-radius: 20px; padding: 25px 15px; text-align: center; border: 2px solid #eee; cursor: pointer; transition: 0.3s; position: relative; }
        .w-card img { width: 55px; margin-bottom: 10px; }
        .w-card h4 { margin: 5px 0; font-size: 24px; color: #fbbf24; }
        .w-card.selected { border-color: orange; background: #fff9f0; }

        /* Important: Withdraw Input Form */
        #withdraw-form { background: #fff; padding: 20px; border-radius: 20px; display: none; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-top: 10px; }
        .input-box { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 15px; font-size: 16px; box-sizing: border-box; outline: none; }
        .submit-btn { width: 100%; background: var(--nagad); color: #fff; border: none; padding: 15px; border-radius: 15px; font-weight: 700; font-size: 16px; cursor: pointer; }

        /* Live Payout Box at bottom of Withdraw */
        .live-payouts { background: #1e293b; color: #fff; border-radius: 20px; padding: 15px; margin-top: 30px; }
        .payout-item { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #334155; font-size: 11px; }

        /* Global Buttons */
        .refer-btn { position: fixed; bottom: 85px; left: 5%; width: 90%; background: var(--primary); color: #000; border: none; padding: 18px; border-radius: 40px; font-weight: 800; font-size: 18px; box-shadow: 0 5px 20px rgba(119,230,33,0.3); z-index: 99; cursor: pointer; }

        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #e2e8f0; z-index: 1000; }
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

    <div id="home" class="page">
        <h3>Available Tasks</h3>
        <div style="background:#fff; padding:20px; border-radius:20px; display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <div><b>{{ task_name }}</b><br><small style="color:var(--primary); font-weight:700;">Reward: ৳15.00</small></div>
            <button style="background:var(--primary); border:none; padding:8px 20px; border-radius:15px; font-weight:700;">Earn</button>
        </div>
    </div>

    <div id="refer" class="page active">
        <div class="refer-dashboard">
            <div class="stat-box"><b>৳0</b><span>Commission</span></div>
            <div class="stat-box"><b>0 <i class="far fa-question-circle" style="color:orange; font-size:10px;"></i></b><span>Pending</span></div>
            <div class="stat-box"><b>99+</b><span>Referrals</span></div>
        </div>

        <div class="podium-container">
            <div class="podium p-2"><div class="gmail-img" style="background:#4caf50;">P</div><b>Pujan</b><br><small>৳4,200</small></div>
            <div class="podium p-1"><i class="fas fa-crown" style="position:absolute; top:-20px; left:38%; color:#fbbf24; font-size:20px;"></i><div class="gmail-img" style="background:#f44336;">M</div><b>Maruf</b><br><small>৳5,800</small></div>
            <div class="podium p-3"><div class="gmail-img" style="background:#2196f3;">S</div><b>Sohag</b><br><small>৳3,500</small></div>
        </div>

        <div class="user-list">
            <div class="user-row"><div style="display:flex; align-items:center; gap:10px;"><div class="gmail-img" style="background:#7c3aed; width:30px; height:30px; margin:0; font-size:12px;">R</div><b>Riyan</b></div><b>৳4479</b></div>
            <div class="user-row"><div style="display:flex; align-items:center; gap:10px;"><div class="gmail-img" style="background:#db2777; width:30px; height:30px; margin:0; font-size:12px;">J</div><b>Julia</b></div><b>৳3920</b></div>
        </div>

        <button class="refer-btn">Refer now</button>
    </div>

    <div id="withdraw" class="page">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
            <b style="font-size: 20px;">Cashout</b>
            <span style="color:#64748b; font-size:14px; font-weight:600;">History <i class="fas fa-chevron-right" style="font-size:10px;"></i></span>
        </div>

        <div class="w-grid">
            <div class="w-card" onclick="openForm(100, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳100</h4>
                <small style="color:#94a3b8; font-size:10px;">1,000,000 Coins</small>
            </div>
            <div class="w-card" onclick="openForm(500, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳500</h4>
                <small style="color:#94a3b8; font-size:10px;">5,000,000 Coins</small>
            </div>
        </div>

        <div id="withdraw-form">
            <h4 id="sel-txt" style="margin-top:0;">Withdraw ৳100</h4>
            <input type="number" class="input-box" placeholder="Enter Nagad Number">
            <button class="submit-btn" onclick="alert('Withdrawal request submitted!')">Withdraw Now</button>
        </div>

        <div class="live-payouts">
            <h5 style="margin:0 0 10px 0; color:var(--primary); font-size:14px;"><i class="fas fa-bolt"></i> Live Withdrawals</h5>
            <div id="live-list">
                </div>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item" onclick="showPage('home', this)"><i class="fas fa-gift"></i>Offerbar</div>
        <div class="nav-item active-nav" onclick="showPage('refer', this)"><i class="fas fa-user-plus"></i>Refer</div>
        <div class="nav-item" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i>Cashout</div>
    </div>

    <script>
        function showPage(id, el) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active-nav'));
            if(el) el.classList.add('active-nav');
        }

        function openForm(amt, el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
            document.getElementById('withdraw-form').style.display = 'block';
            document.getElementById('sel-txt').innerText = "Withdraw ৳" + amt;
            window.scrollTo(0, document.body.scrollHeight);
        }

        // Live Withdraw Animation
        const userNames = ["Maruf", "Julia", "Siyam", "Abir", "Mursalin", "Rifat", "Sumon"];
        function updateLiveList() {
            const list = document.getElementById('live-list');
            const name = userNames[Math.floor(Math.random() * userNames.length)];
            const amt = [100, 200, 500][Math.floor(Math.random() * 3)];
            const item = `<div class="payout-item"><span>${name} withdrawn to Nagad</span> <b>৳${amt}</b></div>`;
            list.innerHTML = item + list.innerHTML;
            if(list.children.length > 5) list.lastElementChild.remove();
        }
        setInterval(updateLiveList, 5000);
        updateLiveList();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, task_name=config['task_name'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
