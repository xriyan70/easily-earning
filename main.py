from flask import Flask, render_template_string

app = Flask(__name__)

# Admin Config
config = {
    "refer_bonus": 5,
    "commission": 5,
    "reward_text": "Earn 15,000 Coins (৳15)"
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
        :root { --primary: #77e621; --nagad: #ed1c24; --bg: #f8fafc; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--bg); padding-bottom: 110px; }
        
        .top-nav { background: #2d3436; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; color: #fff; position: sticky; top: 0; z-index: 100; }
        .coins-badge { background: #b48608; padding: 6px 12px; border-radius: 20px; font-weight: 700; font-size: 14px; border: 1px solid #fbbf24; }

        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* Task Design (Image 22628 style) */
        .task-card { background: #fff; border-radius: 20px; padding: 18px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .earn-btn { background: var(--primary); border: none; padding: 8px 20px; border-radius: 12px; font-weight: 800; cursor: pointer; }

        /* Refer & Leaderboard (Image 22612 style) */
        .refer-stats { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-around; text-align: center; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .stat-box b { font-size: 18px; display: block; }
        .stat-box span { font-size: 11px; color: #64748b; font-weight: 600; }

        .podium-container { display: flex; justify-content: center; align-items: flex-end; gap: 10px; margin: 30px 0; }
        .podium { background: #fff; width: 90px; border-radius: 20px; padding: 15px 5px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
        .p-1 { height: 140px; border-top: 5px solid #fbbf24; transform: scale(1.05); }
        .gmail-img { width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 700; margin: 0 auto 8px; border: 2px solid #fff; }

        /* Withdraw Section (Image 22639 style) */
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
        .w-card { background: #fff; border-radius: 20px; padding: 20px; text-align: center; border: 2px solid #eee; cursor: pointer; }
        .w-card img { width: 40px; margin-bottom: 5px; }
        .w-card.selected { border-color: var(--nagad); background: #fff5f5; }

        .withdraw-form { background: #fff; border-radius: 25px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .input-box { width: 100%; padding: 15px; border-radius: 15px; border: 1px solid #e2e8f0; margin-bottom: 12px; font-size: 16px; box-sizing: border-box; text-align: center; }
        .btn-black { width: 100%; background: #1e293b; color: #fff; border: none; padding: 16px; border-radius: 15px; font-weight: 700; margin-bottom: 10px; cursor: pointer; }
        .btn-green { width: 100%; background: var(--primary); color: #000; border: none; padding: 16px; border-radius: 15px; font-weight: 700; cursor: pointer; }

        /* Live Payout (Professional Style) */
        .live-box { margin-top: 25px; background: #fff; border-radius: 20px; border: 1px solid #e2e8f0; overflow: hidden; }
        .live-row { padding: 12px 15px; border-bottom: 1px dashed #eee; font-size: 12px; display: flex; justify-content: space-between; }
        .live-row b { color: var(--nagad); }

        /* Navigation */
        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #e2e8f0; }
        .nav-item { text-align: center; color: #94a3b8; font-size: 11px; font-weight: 700; cursor: pointer; }
        .active-nav { color: var(--primary); }
    </style>
</head>
<body>

    <div class="top-nav">
        <b>EASILY EARNING</b>
        <div class="coins-badge"><i class="fas fa-coins"></i> 81,480 ≈ ৳81.48</div>
    </div>

    <div id="home" class="page active">
        <h3 style="margin-left:5px;">Tasks</h3>
        <div class="task-card">
            <div><b>Watch & Subscribe 01</b><br><small style="color:var(--primary); font-weight:700;">{{ reward }}</small></div>
            <button class="earn-btn">Earn</button>
        </div>
        <div class="task-card">
            <div><b>YouTube Video Task 02</b><br><small style="color:var(--primary); font-weight:700;">{{ reward }}</small></div>
            <button class="earn-btn">Earn</button>
        </div>
    </div>

    <div id="refer" class="page">
        <div class="refer-stats">
            <div class="stat-box"><b>৳0</b><span>Commission</span></div>
            <div class="stat-box"><b>0</b><span>Pending</span></div>
            <div class="stat-box"><b>0</b><span>Referrals</span></div>
        </div>
        <div class="podium-container">
            <div class="podium"><div class="gmail-img" style="background:#4caf50;">P</div><b>Pujan</b><br><small>৳4,200</small></div>
            <div class="podium p-1"><div class="gmail-img" style="background:#f44336;">M</div><b>Maruf</b><br><small>৳5,800</small></div>
            <div class="podium"><div class="gmail-img" style="background:#2196f3;">S</div><b>Sohag</b><br><small>৳3,500</small></div>
        </div>
        <button style="width:100%; background:var(--primary); border:none; padding:18px; border-radius:40px; font-weight:800; font-size:18px;">Refer now</button>
    </div>

    <div id="withdraw" class="page">
        <h3>Withdraw (Nagad)</h3>
        <div class="w-grid">
            <div class="w-card" onclick="selectCard(100, this)"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png"><h4>৳100</h4></div>
            <div class="w-card selected" onclick="selectCard(200, this)"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png"><h4>৳200</h4></div>
            <div class="w-card" onclick="selectCard(300, this)"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png"><h4>৳300</h4></div>
            <div class="w-card" onclick="selectCard(500, this)"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png"><h4>৳500</h4></div>
        </div>

        <div class="withdraw-form">
            <input type="number" class="input-box" placeholder="Enter Nagad Number" id="num">
            <button class="btn-black" onclick="alert('Withdraw Request Sent!')">Withdraw Now</button>
            <button class="btn-green">Withdraw History</button>
        </div>

        <div class="live-box">
            <div style="background:#f1f5f9; padding:10px 15px; font-weight:700; font-size:13px;">Live Withdrawals</div>
            <div id="live-list"></div>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item active-nav" onclick="showPage('home', this)"><i class="fas fa-home"></i><br>Home</div>
        <div class="nav-item" onclick="showPage('refer', this)"><i class="fas fa-user-friends"></i><br>Refer</div>
        <div class="nav-item" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i><br>Withdraw</div>
    </div>

    <script>
        function showPage(id, el) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active-nav'));
            if(el) el.classList.add('active-nav');
        }
        function selectCard(amt, el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
        }
        function updateLive() {
            const list = document.getElementById('live-list');
            const names = ["Maruf", "Julia", "Siyam", "Abir", "Mursalin"];
            const name = names[Math.floor(Math.random() * names.length)];
            const amt = [100, 200, 500][Math.floor(Math.random() * 3)];
            list.innerHTML = `<div class="live-row"><span>${name}*** withdrawn</span> <b>৳${amt} Nagad</b></div>` + list.innerHTML;
            if(list.children.length > 5) list.lastElementChild.remove();
        }
        setInterval(updateLive, 5000);
        updateLive();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, reward=config['reward_text'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
