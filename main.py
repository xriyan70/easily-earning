from flask import Flask, render_template_string

app = Flask(__name__)

# Admin Config
config = {
    "refer_bonus": 5,
    "commission": 5,
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
        :root { --primary: #77e621; --nagad: #ed1c24; --bg: #f8fafc; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--bg); padding-bottom: 100px; }
        .top-nav { background: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 100; }
        .coins-box { background: #f1f5f9; padding: 6px 15px; border-radius: 20px; font-weight: 700; color: #b45309; font-size: 14px; }
        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        
        .refer-dashboard { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-around; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .stat-box b { font-size: 18px; display: block; color: #000; }
        .stat-box span { font-size: 11px; color: #64748b; font-weight: 600; }

        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
        .w-card { background: #fff; border-radius: 20px; padding: 20px; text-align: center; border: 2px solid #eee; cursor: pointer; position: relative; }
        .w-card img { width: 50px; margin-bottom: 10px; }
        .w-card h4 { margin: 5px 0; font-size: 24px; color: #fbbf24; }
        .w-card.selected { border-color: orange; background: #fff9f0; }

        #withdraw-form { background: #fff; padding: 20px; border-radius: 20px; display: none; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .input-box { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 15px; font-size: 16px; outline: none; box-sizing: border-box; }
        .submit-btn { width: 100%; background: var(--nagad); color: #fff; border: none; padding: 15px; border-radius: 15px; font-weight: 700; font-size: 16px; cursor: pointer; }

        .live-payouts { background: #1e293b; color: #fff; border-radius: 20px; padding: 15px; margin-top: 30px; }
        .payout-item { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #334155; font-size: 11px; }

        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #e2e8f0; z-index: 1000; }
        .nav-item { text-align: center; color: #94a3b8; font-size: 10px; font-weight: 700; cursor: pointer; text-decoration: none; }
        .nav-item i { font-size: 22px; display: block; margin-bottom: 4px; }
        .active-nav { color: var(--primary); }
    </style>
</head>
<body>
    <div class="top-nav">
        <b>EASILY EARNING</b>
        <div class="coins-box"><i class="fas fa-coins"></i> 81,480 ≈ ৳81.48</div>
    </div>

    <div id="home" class="page">
        <h3>Tasks</h3>
        <p>Complete tasks to earn coins.</p>
    </div>

    <div id="refer" class="page active">
        <div class="refer-dashboard">
            <div class="stat-box"><b>৳0</b><span>Commission</span></div>
            <div class="stat-box"><b>0</b><span>Pending</span></div>
            <div class="stat-box"><b>99+</b><span>Referrals</span></div>
        </div>
        <div style="text-align:center;">
             <button style="background:var(--primary); border:none; padding:18px; border-radius:40px; width:90%; font-weight:800; font-size:18px;">Refer now</button>
        </div>
    </div>

    <div id="withdraw" class="page">
        <div class="w-grid">
            <div class="w-card" onclick="openForm(100, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳100</h4>
            </div>
            <div class="w-card" onclick="openForm(500, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳500</h4>
            </div>
        </div>

        <div id="withdraw-form">
            <h4 id="sel-txt">Withdraw ৳100</h4>
            <input type="number" class="input-box" placeholder="Enter Nagad Number">
            <button class="submit-btn" onclick="alert('Withdraw Request Sent!')">Withdraw Now</button>
        </div>

        <div class="live-payouts">
            <h5 style="color:var(--primary);">Live Withdrawals</h5>
            <div id="live-list"></div>
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
        }
        function updateLive() {
            const list = document.getElementById('live-list');
            const amt = [100, 200, 500][Math.floor(Math.random() * 3)];
            list.innerHTML = `<div class="payout-item"><span>User withdrawn to Nagad</span> <b>৳${amt}</b></div>` + list.innerHTML;
            if(list.children.length > 4) list.lastElementChild.remove();
        }
        setInterval(updateLive, 5000);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
