from flask import Flask, render_template_string

app = Flask(__name__)

# Admin Configuration
config = {
    "task_1": "Watch & Subscribe 01",
    "task_2": "YouTube Video Task 02",
    "task_3": "Complete Video Task 03",
    "reward": "15,000 Coins (৳15)"
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
        :root { --primary: #77e621; --nagad: #ed1c24; --dark: #1e293b; --bg: #f8fafc; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--bg); padding-bottom: 100px; color: #334155; }
        
        /* Header */
        .top-nav { background: #2d3436; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; color: #fff; position: sticky; top: 0; z-index: 100; }
        .coins-badge { background: #b48608; padding: 6px 12px; border-radius: 20px; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 5px; border: 1px solid #fbbf24; }

        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* Task Cards (Image 22628 style) */
        .task-card { background: #fff; border-radius: 25px; padding: 20px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #f1f5f9; }
        .task-info b { font-size: 16px; color: #1e293b; display: block; }
        .task-info small { color: var(--primary); font-weight: 700; font-size: 13px; }
        .earn-btn { background: var(--primary); border: none; padding: 10px 25px; border-radius: 15px; font-weight: 800; cursor: pointer; color: #000; }

        /* Withdraw Cards (Image 22639 style) */
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
        .w-card { background: #fff; border-radius: 25px; padding: 20px; text-align: center; border: 2px solid #f1f5f9; cursor: pointer; transition: 0.3s; }
        .w-card img { width: 45px; margin-bottom: 5px; }
        .w-card h4 { margin: 0; font-size: 22px; color: #000; }
        .w-card.selected { border-color: #ed1c24; background: #fff5f5; }

        /* Withdraw Form Section (Always Visible) */
        .withdraw-section { background: #fff; border-radius: 30px; padding: 25px; box-shadow: 0 -5px 25px rgba(0,0,0,0.03); margin-top: 10px; }
        .input-box { width: 100%; padding: 18px; border-radius: 18px; border: 1px solid #e2e8f0; margin-bottom: 15px; font-size: 16px; outline: none; box-sizing: border-box; background: #f8fafc; text-align: center; font-weight: 600; }
        .btn-withdraw { width: 100%; background: #1e293b; color: #fff; border: none; padding: 18px; border-radius: 20px; font-weight: 700; font-size: 16px; margin-bottom: 12px; cursor: pointer; }
        .btn-history { width: 100%; background: var(--primary); color: #000; border: none; padding: 18px; border-radius: 20px; font-weight: 700; font-size: 16px; cursor: pointer; }

        /* Live Payout List (Professional Font & Style) */
        .live-payout-container { margin-top: 30px; background: #fff; border-radius: 20px; border: 1px solid #e2e8f0; overflow: hidden; }
        .live-header { background: #f1f5f9; padding: 12px 20px; font-size: 13px; font-weight: 700; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; }
        .payout-list { max-height: 250px; overflow-y: hidden; }
        .payout-row { display: flex; justify-content: space-between; padding: 12px 20px; border-bottom: 1px dashed #e2e8f0; font-size: 12px; animation: slideDown 0.5s ease; }
        @keyframes slideDown { from { transform: translateY(-100%); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        .payout-row b { color: var(--nagad); }
        .payout-row span { color: #64748b; font-weight: 600; }

        /* Bottom Nav */
        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #fff; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #e2e8f0; z-index: 1000; }
        .nav-item { text-align: center; color: #94a3b8; font-size: 11px; font-weight: 600; cursor: pointer; }
        .nav-item i { font-size: 22px; display: block; margin-bottom: 3px; }
        .active-nav { color: var(--primary); }
    </style>
</head>
<body>

    <div class="top-nav">
        <b style="font-size: 18px; letter-spacing: 1px;">EASILY EARNING</b>
        <div class="coins-badge">
            <i class="fas fa-coins"></i> 81,480 ≈ ৳81.48
        </div>
    </div>

    <div id="home" class="page active">
        <h3 style="margin-left:5px;">Tasks</h3>
        <div class="task-card">
            <div class="task-info"><b>{{ t1 }}</b><small>Earn {{ r }}</small></div>
            <button class="earn-btn">Earn</button>
        </div>
        <div class="task-card">
            <div class="task-info"><b>{{ t2 }}</b><small>Earn {{ r }}</small></div>
            <button class="earn-btn">Earn</button>
        </div>
        <div class="task-card">
            <div class="task-info"><b>{{ t3 }}</b><small>Earn {{ r }}</small></div>
            <button class="earn-btn">Earn</button>
        </div>
    </div>

    <div id="withdraw" class="page">
        <h3 style="margin-bottom: 20px;">Withdraw (Nagad)</h3>
        
        <div class="w-grid">
            <div class="w-card" onclick="selectCard(100, this)">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png">
                <h4>৳100</h4>
            </div>
            <div class="w-card selected" onclick="selectCard(200, this)">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png">
                <h4>৳200</h4>
            </div>
            <div class="w-card" onclick="selectCard(300, this)">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png">
                <h4>৳300</h4>
            </div>
            <div class="w-card" onclick="selectCard(500, this)">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Nagad_Logo.svg/1200px-Nagad_Logo.svg.png">
                <h4>৳500</h4>
            </div>
        </div>

        <div class="withdraw-section">
            <input type="number" class="input-box" placeholder="Enter Nagad Number" id="nagad-num">
            <button class="btn-withdraw" onclick="submitWithdraw()">Withdraw Now</button>
            <button class="btn-history" onclick="alert('Opening History...')">Withdraw History</button>
        </div>

        <div class="live-payout-container">
            <div class="live-header">
                <span><i class="fas fa-bolt" style="color:#fbbf24;"></i> Live Withdrawals</span>
                <span style="color:var(--primary);">● Online</span>
            </div>
            <div class="payout-list" id="payout-list">
                </div>
        </div>
    </div>

    <div id="refer" class="page">
        <h3>Refer Friends</h3>
        <p>Invite friends and earn ৳10 per refer!</p>
    </div>

    <div class="bottom-nav">
        <div class="nav-item active-nav" onclick="showPage('home', this)"><i class="fas fa-home"></i>Home</div>
        <div class="nav-item" onclick="showPage('home', this)"><i class="fas fa-tasks"></i>Tasks</div>
        <div class="nav-item" onclick="showPage('refer', this)"><i class="fas fa-user-friends"></i>Refer</div>
        <div class="nav-item" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i>Withdraw</div>
    </div>

    <script>
        function showPage(id, el) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active-nav'));
            if(el) el.classList.add('active-nav');
        }

        let selectedAmount = 200;
        function selectCard(amt, el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
            selectedAmount = amt;
        }

        function submitWithdraw() {
            const num = document.getElementById('nagad-num').value;
            if(num.length < 11) {
                alert("Please enter a valid 11-digit Nagad number");
            } else {
                alert(`Request for ৳${selectedAmount} sent for number: ${num}`);
            }
        }

        const names = ["Maruf", "Siyam", "Pujan", "Abir", "Rifat", "Mursalin", "Joy", "Anik"];
        function addLivePayout() {
            const list = document.getElementById('payout-list');
            const name = names[Math.floor(Math.random() * names.length)];
            const amt = [100, 200, 300, 500][Math.floor(Math.random() * 4)];
            const row = `<div class="payout-row">
                            <span>${name}*** just withdrawn</span>
                            <b>৳${amt} to Nagad</b>
                         </div>`;
            list.innerHTML = row + list.innerHTML;
            if(list.children.length > 6) list.lastElementChild.remove();
        }
        setInterval(addLivePayout, 4000);
        addLivePayout();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, t1=config['task_1'], t2=config['task_2'], t3=config['task_3'], r=config['reward'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
