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

        /* Referral Stats (Image 22610) */
        .refer-dashboard { background: #fff; border-radius: 20px; padding: 20px; display: flex; justify-content: space-around; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .stat-box b { font-size: 18px; display: block; color: #000; }
        .stat-box span { font-size: 11px; color: #64748b; font-weight: 600; }

        /* Referral User List (Image 22612) */
        .user-list-card { background: #fff; border-radius: 20px; padding: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); }
        .user-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #f1f5f9; }
        .user-info { display: flex; align-items: center; gap: 10px; }
        .badge { background: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 5px; font-size: 10px; font-weight: 700; }
        .avatar { width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: 700; font-size: 14px; }

        /* Withdraw Cards (Image 22614) */
        .w-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
        .w-card { background: #fff; border-radius: 20px; padding: 20px; text-align: center; border: 2px solid #eee; cursor: pointer; position: relative; overflow: hidden; }
        .w-card img { width: 50px; margin-bottom: 10px; }
        .w-card h4 { margin: 5px 0; font-size: 24px; color: #fbbf24; }
        .w-card.selected { border-color: orange; background: #fff9f0; }
        .w-card .coin-tag { background: #475569; color: #fff; font-size: 10px; padding: 4px; position: absolute; bottom: 0; left: 0; width: 100%; }

        /* Withdraw Form (Input added here) */
        #withdraw-form { background: #fff; padding: 20px; border-radius: 20px; margin-top: 10px; display: none; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        .input-box { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 15px; font-size: 16px; outline: none; box-sizing: border-box; }
        .submit-btn { width: 100%; background: var(--nagad); color: #fff; border: none; padding: 15px; border-radius: 15px; font-weight: 700; font-size: 16px; cursor: pointer; }

        /* Live Payouts at Bottom */
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
        <b style="font-size: 18px;">EASILY EARNING</b>
        <div class="coins-box"><i class="fas fa-coins"></i> 81,480 ≈ ৳81.48</div>
    </div>

    <div id="refer" class="page active">
        <div class="refer-dashboard">
            <div class="stat-box"><b>0</b><span>Commission</span></div>
            <div class="stat-box"><b>0 <i class="far fa-question-circle" style="color:orange;"></i></b><span>Pending</span></div>
            <div class="stat-box"><b>0</b><span>Referrals</span></div>
        </div>

        <div class="user-list-card">
            <div style="display:flex; justify-content:space-between; font-size:12px; color:#64748b; margin-bottom:10px; font-weight:600;">
                <span># User</span><span>Referrals</span><span>Commission</span>
            </div>
            <div class="user-row" style="background:#f0fdf4; border-radius:10px; padding:8px 10px;">
                <div class="user-info">
                    <span style="font-size:11px; font-weight:700; color:#16a34a;">99+</span>
                    <div class="avatar" style="background:#7c3aed;">X</div>
                    <b style="font-size:13px;">X Riyan</b> <span class="badge">Me</span>
                </div>
                <b>0</b><b>0</b>
            </div>
            <div class="user-row">
                <div class="user-info"><span>4</span><div class="avatar" style="background:#db2777;">J</div><b>Julia</b></div>
                <b>4626</b><b>৳4479.81</b>
            </div>
            <div class="user-row">
                <div class="user-info"><span>5</span><div class="avatar" style="background:#059669;">B</div><b>Brein</b></div>
                <b>4605</b><b>৳4459.48</b>
            </div>
        </div>

        <div style="text-align:center; margin-top:20px;">
            <button style="background:var(--primary); border:none; padding:18px; border-radius:40px; width:90%; font-weight:800; font-size:18px; box-shadow: 0 5px 20px rgba(119,230,33,0.3);">Refer now</button>
        </div>
    </div>

    <div id="withdraw" class="page">
        <div class="w-header">
            <b style="font-size: 20px;">Withdrawable</b>
            <a href="#" style="color:#64748b; text-decoration:none; font-size:14px; font-weight:600;">History <i class="fas fa-chevron-right"></i></a>
        </div>

        <div class="w-grid">
            <div class="w-card" onclick="openForm(100, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳100</h4>
                <div class="coin-tag">1000000</div>
            </div>
            <div class="w-card" onclick="openForm(200, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳200</h4>
                <div class="coin-tag">2000000</div>
            </div>
            <div class="w-card" onclick="openForm(300, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳300</h4>
                <div class="coin-tag">3000000</div>
            </div>
            <div class="w-card" onclick="openForm(500, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <h4>৳500</h4>
                <div class="coin-tag">5000000</div>
            </div>
        </div>

        <div id="withdraw-form">
            <h4 id="sel-txt" style="margin-top:0;">Withdraw ৳100</h4>
            <input type="number" class="input-box" placeholder="Enter Nagad Number">
            <button class="submit-btn" onclick="alert('Withdraw Request Sent!')">Withdraw Now</button>
        </div>

        <div class="live-payouts">
            <h5 style="margin:0 0 10px 0; color:var(--primary);"><i class="fas fa-bolt"></i> Live Withdrawals</h5>
            <div id="live-list"></div>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-item" onclick="showPage('home', this)"><i class="fas fa-gift"></i>Offer</div>
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

        function openForm(amt, el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
            document.getElementById('withdraw-form').style.display = 'block';
            document.getElementById('sel-txt').innerText = "Withdraw ৳" + amt;
            window.scrollTo(0, document.body.scrollHeight);
        }

        const names = ["Maruf", "Julia", "Siyam", "Abir", "Mursalin", "Rifat"];
        function updateLive() {
            const list = document.getElementById('live-list');
            const name = names[Math.floor(Math.random() * names.length)];
            const amt = [100, 200, 500][Math.floor(Math.random() * 3)];
            const item = `<div class="payout-item"><span>${name} withdrawn to Nagad</span> <b>৳${amt}</b></div>`;
            list.innerHTML = item + list.innerHTML;
            if(list.children.length > 5) list.lastElementChild.remove();
        }
        setInterval(updateLive, 5000);
        updateLive();
    </script>
</body>
</html>
