from flask import Flask, render_template_string, request

app = Flask(__name__)

config = {
    "task_name": "Watch & Subscribe",
    "task_reward": 15000,
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
    <title>Easily Earning</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root { --primary: #77e621; --dark: #1a1c24; --nagad: #ed1c24; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: #f4f7f6; padding-bottom: 80px; overflow-x: hidden; }
        
        .top-nav { background: #2d2f3b; color: white; padding: 15px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; }
        .coins { background: rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 20px; color: #fbbf24; font-weight: bold; }

        .page { display: none; padding: 15px; animation: slideUp 0.3s ease; }
        .active { display: block; }
        @keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

        /* Fake Notification */
        #withdraw-pop { position: fixed; bottom: 85px; left: 50%; transform: translateX(-50%); background: #333; color: white; padding: 8px 15px; border-radius: 30px; font-size: 11px; z-index: 2000; display: none; white-space: nowrap; border: 1px solid var(--primary); }

        /* Home Task Cards */
        .task-card { background: white; padding: 15px; border-radius: 15px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .earn-btn { background: var(--primary); border: none; padding: 7px 15px; border-radius: 15px; font-weight: bold; cursor: pointer; }

        /* Leaderboard */
        .leaderboard { display: flex; justify-content: center; align-items: flex-end; gap: 10px; margin: 20px 0; }
        .rank { background: white; width: 95px; border-radius: 15px; text-align: center; padding: 10px 5px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
        .rank img { width: 45px; height: 45px; border-radius: 50%; object-fit: cover; border: 2px solid var(--primary); margin-bottom: 5px; }
        .r-1 { height: 140px; border-top: 5px solid #fbbf24; }
        .r-2 { height: 110px; border-top: 5px solid #cbd5e1; }
        .r-3 { height: 95px; border-top: 5px solid #cd7f32; }

        .btn-big { background: var(--primary); color: #000; border: none; padding: 15px; border-radius: 30px; width: 100%; font-weight: 800; font-size: 16px; margin-top: 15px; cursor: pointer; box-shadow: 0 5px 15px rgba(119, 230, 33, 0.3); }

        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        .w-item { background: white; padding: 20px; border-radius: 20px; text-align: center; border: 2px solid transparent; cursor: pointer; }
        .w-item img { width: 60px; margin-bottom: 10px; }
        .w-item.selected { border-color: var(--nagad); background: #fff5f5; }

        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #eee; }
        .nav-link { text-align: center; color: #9ca3af; font-size: 10px; cursor: pointer; flex: 1; text-decoration: none; }
        .nav-link i { font-size: 20px; display: block; margin-bottom: 3px; }
        .active-nav { color: var(--primary); font-weight: bold; }
    </style>
</head>
<body>

    <div id="withdraw-pop"></div>

    <div class="top-nav">
        <div style="font-weight: 700;">EASILY EARNING</div>
        <div class="coins"><i class="fas fa-coins"></i> 81,480 ≈ ৳81.48</div>
    </div>

    <div id="home" class="page active">
        <h3 style="margin-left: 5px;">All Tasks</h3>
        <div class="task-card">
            <div><b>Video Task 01</b><br><small style="color:var(--primary)">Earn 15,000 Coins</small></div>
            <button class="earn-btn" onclick="showPage('tasks', 1)">Earn</button>
        </div>
        <div class="task-card">
            <div><b>Video Task 02</b><br><small style="color:var(--primary)">Earn 15,000 Coins</small></div>
            <button class="earn-btn" onclick="showPage('tasks', 1)">Earn</button>
        </div>
        <div class="task-card">
            <div><b>Video Task 03</b><br><small style="color:var(--primary)">Earn 15,000 Coins</small></div>
            <button class="earn-btn" onclick="showPage('tasks', 1)">Earn</button>
        </div>
    </div>

    <div id="tasks" class="page">
        <h3>Task Center</h3>
        <div style="background: white; padding: 30px; border-radius: 25px; text-align: center;">
            <i class="fab fa-youtube" style="font-size: 60px; color: #ef4444; margin-bottom: 15px;"></i>
            <p>পুরো ভিডিওটি দেখলে আপনি ১৫ টাকা পাবেন।</p>
            <button class="btn-big" onclick="alert('Task Started!')">Watch Video</button>
        </div>
    </div>

    <div id="refer" class="page">
        <h3 style="text-align: center; margin-bottom: 10px;">Top Referrers</h3>
        <div class="leaderboard">
            <div class="rank r-2">
                <img src="https://i.pravatar.cc/150?u=2" alt="p2">
                <div style="font-size: 11px; font-weight: bold;">Siyam</div>
                <div style="color: var(--nagad); font-size: 10px;">৳4,200</div>
            </div>
            <div class="rank r-1">
                <img src="https://i.pravatar.cc/150?u=1" alt="p1">
                <div style="font-size: 12px; font-weight: bold;">Maruf</div>
                <div style="color: var(--nagad); font-size: 11px;">৳5,800</div>
            </div>
            <div class="rank r-3">
                <img src="https://i.pravatar.cc/150?u=3" alt="p3">
                <div style="font-size: 11px; font-weight: bold;">Sohag</div>
                <div style="color: var(--nagad); font-size: 10px;">৳3,500</div>
            </div>
        </div>

        <button class="btn-big" onclick="alert('Link Copied!')">REFER NOW</button>
        
        <div style="display: flex; justify-content: center; gap: 25px; margin-top: 25px;">
            <a href="{{ tg_link }}" style="color: #229ED9; font-size: 30px;"><i class="fab fa-telegram"></i></a>
            <a href="{{ fb_link }}" style="color: #1877F2; font-size: 30px;"><i class="fab fa-facebook"></i></a>
        </div>
    </div>

    <div id="withdraw" class="page">
        <h3>Withdraw (Nagad)</h3>
        <div class="w-grid">
            <div class="w-item" onclick="selW(100, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <b>৳100</b>
            </div>
            <div class="w-item" onclick="selW(200, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <b>৳200</b>
            </div>
            <div class="w-item" onclick="selW(300, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <b>৳300</b>
            </div>
            <div class="w-item" onclick="selW(500, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png">
                <b>৳500</b>
            </div>
        </div>
        <div id="w-form" style="display:none; margin-top:20px; background:white; padding:20px; border-radius:20px;">
            <input type="number" placeholder="Enter Nagad Number" style="width:100%; padding:15px; border-radius:12px; border:1px solid #ddd; outline:none; box-sizing:border-box;">
            <button class="btn-big" style="background:var(--nagad); color:white; margin-top:10px;">Withdraw Now</button>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="nav-link active-nav" onclick="showPage('home', this)"><i class="fas fa-home"></i>Home</div>
        <div class="nav-link" onclick="showPage('tasks', this)"><i class="fas fa-tasks"></i>Tasks</div>
        <div class="nav-link" onclick="showPage('refer', this)"><i class="fas fa-users"></i>Refer</div>
        <div class="nav-link" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i>Withdraw</div>
    </div>

    <script>
        function showPage(id, el) {
            if(typeof el === 'number') el = document.querySelectorAll('.nav-link')[el];
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-link').forEach(n => n.classList.remove('active-nav'));
            el.classList.add('active-nav');
        }

        function selW(amt, el) {
            document.querySelectorAll('.w-item').forEach(i => i.classList.remove('selected'));
            el.classList.add('selected');
            document.getElementById('w-form').style.display = 'block';
        }

        // Fake Withdraw Notifications
        const names = ["Siyam", "Abir", "Mursalin", "Rifat", "Sumon", "Ariful", "Maruf"];
        const amounts = [100, 200, 300, 500];
        
        setInterval(() => {
            const name = names[Math.floor(Math.random() * names.length)];
            const amt = amounts[Math.floor(Math.random() * amounts.length)];
            const pop = document.getElementById('withdraw-pop');
            pop.innerHTML = `<i class="fas fa-check-circle" style="color:var(--primary)"></i> ${name} has withdrawn ৳${amt} to Nagad`;
            pop.style.display = 'block';
            setTimeout(() => { pop.style.display = 'none'; }, 4000);
        }, 8000);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, tg_link=config['tg_link'], fb_link=config['fb_link'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
