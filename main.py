from flask import Flask, render_template_string

app = Flask(__name__)

config = {
    "task_name": "Watch & Subscribe - 01",
    "refer_bonus": 5,
    "commission": 5,
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
        
        .top-nav { background: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 100; }
        .coins-box { background: #f1f5f9; padding: 6px 15px; border-radius: 20px; font-weight: 700; color: #b45309; font-size: 14px; }

        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* Task & Refer (Previous Style Maintained) */
        .task-card { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
        .refer-dashboard { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-around; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .podium-container { display: flex; justify-content: center; align-items: flex-end; gap: 12px; margin: 35px 0 20px; }
        .podium { background: #fff; width: 95px; border-radius: 20px; padding: 15px 5px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
        .p-1 { height: 145px; border-top: 5px solid #fbbf24; transform: scale(1.1); }
        .gmail-img { width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 700; margin: 0 auto 10px; border: 2px solid #fff; }

        /* Withdraw Grid with Nagad Logo */
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px; }
        .w-card { background: #fff; border-radius: 20px; padding: 15px; text-align: center; border: 2px solid #eee; cursor: pointer; transition: 0.3s; }
        .w-card img { width: 45px; height: 45px; object-fit: contain; margin-bottom: 8px; }
        .w-card h4 { margin: 0; font-size: 20px; color: #000; }
        .w-card.selected { border-color: var(--nagad); background: #fff5f5; }

        /* Form Section */
        .withdraw-form { background: #fff; padding: 25px; border-radius: 25px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); }
        .input-box { width: 100%; padding: 16px; border-radius: 15px; border: 1px solid #e2e8f0; margin-bottom: 15px; font-size: 16px; box-sizing: border-box; outline: none; text-align: center; }
        .submit-btn { width: 100%; background: var(--nagad); color: #fff; border: none; padding: 16px; border-radius: 15px; font-weight: 700; cursor: pointer; }
        .history-btn { width: 100%; background: var(--primary); color: #000; border: none; padding: 16px; border-radius: 15px; font-weight: 700; margin-top: 10px; cursor: pointer; }

        /* Professional Payout List */
        .live-payouts { background: #1e293b; color: #fff; border-radius: 25px; padding: 20px; margin-top: 25px; }
        .payout-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #334155; font-size: 12px; }
        .payout-item b { color: var(--primary); }

        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #e2e8f0; z-index: 1000; }
        .nav-item { text-align: center; color: #94a3b8; font-size: 11px; font-weight: 700; cursor: pointer; }
        .active-nav { color: var(--primary); }
    </style>
</head>
<body>

    <div class="top-nav">
        <b>EASILY EARNING</b>
        <div class="coins-box"><i class="fas fa-coins"></i> 0.00 ≈ ৳0.00</div>
    </div>

    <div id="home" class="page">
        <h3 style="margin-left:5px;">Offerbar</h3>
        <div class="task-card">
            <div><b>{{ task_name }}</b><br><small style="color:var(--primary); font-weight:700;">Reward: ৳15.00</small></div>
            <button style="background:var(--primary); border:none; padding:8px 20px; border-radius:15px; font-weight:700;">Earn</button>
        </div>
    </div>

    <div id="refer" class="page active">
        <div class="refer-dashboard">
            <div class="stat-box"><b>৳0</b><span>Commission</span></div>
            <div class="stat-box"><b>0</b><span>Pending</span></div>
            <div class="stat-box"><b>৳5</b><span>Per Refer</span></div>
        </div>
        <div class="podium-container">
            <div class="podium"><div class="gmail-img" style="background:#4caf50;">P</div><b>Pujan</b></div>
            <div class="podium p-1"><div class="gmail-img" style="background:#f44336;">M</div><b>Maruf</b></div>
            <div class="podium"><div class="gmail-img" style="background:#2196f3;">S</div><b>Sohag</b></div>
        </div>
        <button style="width:100%; background:var(--primary); border:none; padding:18px; border-radius:40px; font-weight:800; font-size:18px;">Refer now</button>
    </div>

    <div id="withdraw" class="page">
        <h3 style="margin-bottom:15px;">Withdraw (Nagad)</h3>
        <div class="w-grid">
            <div class="w-card" onclick="selectAmt(100, this)"><img src="https://itshams.com/wp-content/uploads/2023/07/Nagad-App-Logo-Vector.png"><h4>৳100</h4></div>
            <div class="w-card selected" onclick="selectAmt(200, this)"><img src="https://itshams.com/wp-content/uploads/2023/07/Nagad-App-Logo-Vector.png"><h4>৳200</h4></div>
            <div class="w-card" onclick="selectAmt(300, this)"><img src="https://itshams.com/wp-content/uploads/2023/07/Nagad-App-Logo-Vector.png"><h4>৳300</h4></div>
            <div class="w-card" onclick="selectAmt(500, this)"><img src="https://itshams.com/wp-content/uploads/2023/07/Nagad-App-Logo-Vector.png"><h4>৳500</h4></div>
        </div>

        <div class="withdraw-form">
            <h4 id="sel-txt" style="margin:0 0 10px 0; text-align:center;">Selected: ৳200</h4>
            <input type="number" class="input-box" placeholder="Enter Nagad Number">
            <button class="submit-btn" onclick="alert('Success!')">Withdraw Now</button>
            <button class="history-btn">Withdraw History</button>
        </div>

        <div class="live-payouts">
            <div style="color:var(--primary); font-size:14px; font-weight:700; margin-bottom:10px;"><i class="fas fa-bolt"></i> LIVE PAYOUT HISTORY</div>
            <div id="live-list"></div>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item" onclick="showPage('home', this)"><i class="fas fa-gift"></i><br>Offerbar</div>
        <div class="nav-item active-nav" onclick="showPage('refer', this)"><i class="fas fa-user-plus"></i><br>Refer</div>
        <div class="nav-item" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i><br>Cashout</div>
    </div>

    <script>
        function showPage(id, el) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active-nav'));
            if(el) el.classList.add('active-nav');
        }
        function selectAmt(amt, el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
            document.getElementById('sel-txt').innerText = "Selected: ৳" + amt;
        }
        function updateLive() {
            const list = document.getElementById('live-list');
            const names = ["Maruf", "Julia", "Siyam", "Abir", "Mursalin"];
            const name = names[Math.floor(Math.random() * names.length)];
            const amt = [100, 200, 300, 500][Math.floor(Math.random() * 4)];
            list.innerHTML = `<div class="payout-item"><span>${name}*** withdrawn</span> <b>৳${amt}</b></div>` + list.innerHTML;
            if(list.children.length > 5) list.lastElementChild.remove();
        }
        setInterval(updateLive, 4000);
        updateLive();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, task_name=config['task_name'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
