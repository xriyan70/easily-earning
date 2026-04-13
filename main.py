from flask import Flask, render_template_string

app = Flask(__name__)

# Config Section
config = {
    "refer_bonus": 5,
    "commission": 5,
    "min_tasks_required": 2
}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Easily Earning</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root { --primary: #77e621; --nagad: #ed1c24; --bg: #f8fafc; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--bg); padding-bottom: 80px; }
        
        /* Navbar Style */
        .top-nav { background: #2d3436; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; color: #fff; position: sticky; top: 0; z-index: 100; }
        .coins-badge { background: #b48608; padding: 6px 12px; border-radius: 20px; font-weight: 700; font-size: 14px; border: 1px solid #fbbf24; }

        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* Leaderboard Style */
        .podium-container { display: flex; justify-content: center; align-items: flex-end; gap: 10px; margin: 30px 0; }
        .podium { background: #fff; width: 90px; border-radius: 20px; padding: 15px 5px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); position: relative; }
        .p-1 { height: 140px; border-top: 5px solid #fbbf24; transform: scale(1.05); }
        .user-avatar { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #fff; margin: 0 auto 8px; }

        /* Referral */
        .refer-stats { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-around; text-align: center; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .stat-box b { font-size: 18px; display: block; }
        .stat-box span { font-size: 11px; color: #64748b; font-weight: 600; }

        /* Withdrawal Grid */
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        .w-card { background: #fff; border-radius: 20px; padding: 20px; text-align: center; border: 2px solid #eee; display: flex; flex-direction: column; align-items: center; }
        .w-card img { width: 40px; height: auto; margin-bottom: 8px; display: block; }
        .w-card b { font-size: 18px; }
        
        .input-box { width: 100%; padding: 15px; border-radius: 15px; border: 1px solid #e2e8f0; margin: 15px 0; box-sizing: border-box; outline: none; }
        .btn-black { width: 100%; background: #1e293b; color: #fff; padding: 16px; border-radius: 15px; border: none; font-weight: 700; margin-bottom: 10px; cursor: pointer; }
        .btn-green { width: 100%; background: var(--primary); color: #000; padding: 16px; border-radius: 15px; border: none; font-weight: 700; cursor: pointer; }

        /* Bottom Nav */
        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #eee; z-index: 1000; }
        .nav-item { text-align: center; color: #94a3b8; font-size: 11px; cursor: pointer; }
        .active-nav { color: var(--primary); }
    </style>
</head>
<body>

    <div class="top-nav">
        <b>EASILY EARNING</b>
        <div class="coins-badge"><i class="fas fa-coins"></i> 81,480 ≈ ৳81.48</div>
    </div>

    <div id="home" class="page active">
        <h3>Welcome Home</h3>
        <p>Start completing tasks and invite friends to earn more!</p>
    </div>

    <div id="tasks" class="page">
        <h3>Tasks</h3>
        <div style="background:#fff; border-radius:20px; padding:20px; display:flex; justify-content:space-between; align-items:center;">
            <div><b>Watch & Subscribe 01</b><br><small style="color:var(--primary); font-weight:700;">Earn 15,000 Coins (৳15)</small></div>
            <button style="background:var(--primary); border:none; padding:8px 20px; border-radius:12px; font-weight:800;">Earn</button>
        </div>
    </div>

    <div id="refer" class="page">
        <div class="refer-stats">
            <div class="stat-box"><b>৳0</b><span>Commission</span></div>
            <div class="stat-box"><b>0</b><span>Pending</span></div>
            <div class="stat-box"><b>0</b><span>Referrals</span></div>
        </div>

        <div class="podium-container">
            <div class="podium"><div style="background:#4caf50;" class="user-avatar"></div><b>Pujan</b><br><small>৳4,200</small></div>
            <div class="podium p-1"><div style="background:#f44336;" class="user-avatar"></div><b>Maruf</b><br><small>৳5,800</small></div>
            <div class="podium"><div style="background:#2196f3;" class="user-avatar"></div><b>Sohag</b><br><small>৳3,500</small></div>
        </div>
        
        <p style="font-size:11px; color:orange; text-align:center;">* Referred friends must complete 2 tasks for you to get ৳5 reward.</p>
        <button style="width:100%; background:var(--primary); border:none; padding:18px; border-radius:40px; font-weight:800; font-size:18px;">Refer now</button>
    </div>

    <div id="withdraw" class="page">
        <h3 style="margin-top:0;">Withdraw (Nagad)</h3>
        <div class="w-grid">
            <div class="w-card"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Nagad_Logo.svg/1024px-Nagad_Logo.svg.png"><b>৳100</b></div>
            <div class="w-card" style="border-color:red; background:#fff5f5;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Nagad_Logo.svg/1024px-Nagad_Logo.svg.png"><b>৳200</b></div>
            <div class="w-card"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Nagad_Logo.svg/1024px-Nagad_Logo.svg.png"><b>৳300</b></div>
            <div class="w-card"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Nagad_Logo.svg/1024px-Nagad_Logo.svg.png"><b>৳500</b></div>
        </div>
        <div style="background:#fff; border-radius:25px; padding:20px; margin-top:20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <input type="number" class="input-box" placeholder="Enter Nagad Number">
            <button class="btn-black">Withdraw Now</button>
            <button class="btn-green">Withdraw History</button>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item active-nav" onclick="showPage('home', this)"><i class="fas fa-home"></i><br>Home</div>
        <div class="nav-item" onclick="showPage('tasks', this)"><i class="fas fa-list-ul"></i><br>Tasks</div>
        <div class="nav-item" onclick="showPage('refer', this)"><i class="fas fa-user-friends"></i><br>Refer</div>
        <div class="nav-item" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i><br>Withdraw</div>
    </div>

    <script>
        function showPage(id, el) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active-nav'));
            el.classList.add('active-nav');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
