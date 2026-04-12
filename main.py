from flask import Flask, render_template_string, request

app = Flask(__name__)

# অ্যাডমিন কনফিগারেশন - এখান থেকে সব কন্ট্রোল হবে
config = {
    "task_name": "Watch & Subscribe",
    "task_reward_coins": 15000, # ১৫০০০ কয়েন = ১৫ টাকা
    "refer_reward_tk": 5,
    "tg_link": "https://t.me/your_channel", # এখানে তোমার টেলিগ্রাম লিংক দাও
    "fb_link": "https://facebook.com/your_group", # এখানে তোমার ফেসবুক লিংক দাও
    "admin_pass": "maruf786" # তোমার অ্যাডমিন পাসওয়ার্ড
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
        :root { --primary: #77e621; --dark: #1a1c24; --nagad: #ed1c24; --gold: #fbbf24; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: #f8fafc; padding-bottom: 90px; }
        
        .top-nav { background: #2d2f3b; color: white; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; }
        .coins { background: rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 20px; font-weight: bold; color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3); }

        .page { display: none; padding: 15px; animation: fadeIn 0.3s ease; }
        .active { display: block; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* Leaderboard 3D Style */
        .leaderboard-top { display: flex; justify-content: center; align-items: flex-end; gap: 10px; margin: 30px 0; }
        .rank-box { background: white; width: 90px; border-radius: 15px; text-align: center; padding: 10px 5px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); position: relative; }
        .rank-2 { height: 100px; border-top: 4px solid #cbd5e1; }
        .rank-1 { height: 130px; border-top: 4px solid var(--gold); transform: scale(1.1); z-index: 2; }
        .rank-3 { height: 90px; border-top: 4px solid #cd7f32; }
        .crown { position: absolute; top: -18px; left: 50%; transform: translateX(-50%); color: var(--gold); font-size: 20px; }

        .stat-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 20px; }
        .stat-card { background: white; padding: 15px 5px; border-radius: 15px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
        .stat-card h2 { margin: 0; font-size: 18px; }
        .stat-card p { margin: 5px 0 0; font-size: 10px; color: #6b7280; font-weight: 600; }

        .btn-main { background: var(--primary); color: #000; border: none; padding: 15px; border-radius: 30px; width: 100%; font-weight: 800; font-size: 16px; box-shadow: 0 4px 15px rgba(119, 230, 33, 0.4); cursor: pointer; }
        
        .social-links { display: flex; justify-content: center; gap: 20px; margin-top: 20px; }
        .social-btn { width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; text-decoration: none; }

        .w-card { background: white; padding: 20px; border-radius: 20px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 2px solid transparent; cursor: pointer; }
        .w-card.selected { border-color: var(--nagad); background: #fff5f5; }

        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #e5e7eb; }
        .n-item { text-align: center; color: #9ca3af; font-size: 10px; cursor: pointer; flex: 1; }
        .n-item i { font-size: 20px; display: block; margin-bottom: 4px; }
        .active-nav { color: var(--primary); font-weight: bold; }
    </style>
</head>
<body>

    <div class="top-nav">
        <div style="font-weight: 700;">EASILY EARNING</div>
        <div class="coins"><i class="fas fa-coins"></i> 81480 ≈ ৳81.48</div>
    </div>

    <div id="home" class="page active">
        <h3>Available Tasks</h3>
        <div style="background: white; padding: 20px; border-radius: 20px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center;">
                <div style="width: 45px; height: 45px; background: #fee2e2; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                    <i class="fab fa-youtube" style="color: #ef4444; font-size: 24px;"></i>
                </div>
                <div>
                    <div style="font-weight: 700; font-size: 14px;">{{ task_name }}</div>
                    <div style="color: var(--primary); font-size: 12px; font-weight: bold;">Earn {{ task_reward }} Coins</div>
                </div>
            </div>
            <button onclick="showPage('tasks', document.querySelectorAll('.n-item')[1])" style="background: var(--primary); border: none; padding: 8px 15px; border-radius: 20px; font-weight: bold;">Earn</button>
        </div>
    </div>

    <div id="tasks" class="page">
        <h3>Task Center</h3>
        <div style="background: white; padding: 30px; border-radius: 25px; text-align: center;">
            <i class="fas fa-tasks" style="font-size: 50px; color: var(--primary); margin-bottom: 15px;"></i>
            <p>টাস্কটি সম্পন্ন করলে আপনি {{ task_reward }} কয়েন পাবেন।</p>
            <button class="btn-main">Complete Task</button>
        </div>
    </div>

    <div id="refer" class="page">
        <h3 style="text-align: center; margin: 0;">Leaderboard</h3>
        <div class="leaderboard-top">
            <div class="rank-box rank-2">
                <div style="font-weight: bold; font-size: 12px;">Siyam</div>
                <div style="color: var(--nagad); font-size: 11px;">৳4,200</div>
            </div>
            <div class="rank-box rank-1">
                <i class="fas fa-crown crown"></i>
                <div style="font-weight: bold; font-size: 14px;">Maruf</div>
                <div style="color: var(--nagad); font-size: 12px;">৳5,800</div>
            </div>
            <div class="rank-box rank-3">
                <div style="font-weight: bold; font-size: 12px;">Sohag</div>
                <div style="color: var(--nagad); font-size: 11px;">৳3,500</div>
            </div>
        </div>

        <div class="stat-grid">
            <div class="stat-card"><h2>0</h2><p>Commission</p></div>
            <div class="stat-card"><h2>0</h2><p>Pending</p></div>
            <div class="stat-card"><h2>0</h2><p>Referrals</p></div>
        </div>

        <button class="btn-main" onclick="alert('Refer Link Copied!')">Refer Now</button>
        <p style="text-align: center; font-size: 11px; color: #9ca3af; margin-top: 10px;">Link: https://easilyearning.com/ref/user786</p>

        <div class="social-links">
            <a href="{{ tg_link }}" class="social-btn" style="background: #229ED9;"><i class="fab fa-telegram-plane"></i></a>
            <a href="{{ fb_link }}" class="social-btn" style="background: #1877F2;"><i class="fab fa-facebook-f"></i></a>
        </div>
    </div>

    <div id="withdraw" class="page">
        <h3>Withdraw (Nagad)</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div class="w-card" onclick="selectW(100, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png" width="50"><br>
                <b>৳100</b><br><small>100,000 Coins</small>
            </div>
            <div class="w-card" onclick="selectW(500, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png" width="50"><br>
                <b>৳500</b><br><small>500,000 Coins</small>
            </div>
        </div>
        <div id="w-form" style="display:none; margin-top:20px;">
            <input type="number" placeholder="Enter Nagad Number" style="width:100%; padding:15px; border-radius:15px; border:1px solid #ddd; box-sizing: border-box;">
            <button class="btn-main" style="background: var(--nagad); color: white; margin-top:15px;">Withdraw Now</button>
        </div>
    </div>

    <div class="bottom-nav">
        <div class="n-item active-nav" onclick="showPage('home', this)"><i class="fas fa-home"></i>Home</div>
        <div class="n-item" onclick="showPage('tasks', this)"><i class="fas fa-clipboard-check"></i>Tasks</div>
        <div class="n-item" onclick="showPage('refer', this)"><i class="fas fa-user-friends"></i>Refer</div>
        <div class="n-item" onclick="showPage('withdraw', this)"><i class="fas fa-wallet"></i>Withdraw</div>
    </div>

    <script>
        function showPage(id, el) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.n-item').forEach(n => n.classList.remove('active-nav'));
            el.classList.add('active-nav');
        }
        function selectW(amt, el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
            document.getElementById('w-form').style.display = 'block';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, 
                                  task_name=config['task_name'], 
                                  task_reward=config['task_reward_coins'],
                                  tg_link=config['tg_link'],
                                  fb_link=config['fb_link'])

@app.route('/admin_control', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('pass') == config['admin_pass']:
            config['task_name'] = request.form.get('t_name')
            config['task_reward_coins'] = int(request.form.get('t_reward'))
            config['tg_link'] = request.form.get('tg')
            config['fb_link'] = request.form.get('fb')
            return "সব আপডেট হয়েছে! <a href='/'>হোম পেজে যান</a>"
        return "ভুল পাসওয়ার্ড!"
    
    return f'''
    <div style="padding:20px; font-family: sans-serif;">
        <h2>Easily Earning Admin</h2>
        <form method="post">
            পাসওয়ার্ড: <input type="password" name="pass"><br><br>
            টাস্ক নাম: <input type="text" name="t_name" value="{config['task_name']}"><br><br>
            রিওয়ার্ড কয়েন: <input type="number" name="t_reward" value="{config['task_reward_coins']}"><br><br>
            টেলিগ্রাম লিংক: <input type="text" name="tg" value="{config['tg_link']}"><br><br>
            ফেসবুক লিংক: <input type="text" name="fb" value="{config['fb_link']}"><br><br>
            <button type="submit" style="padding:10px 20px; background: green; color:white; border:none; border-radius:5px;">সেভ করুন</button>
        </form>
    </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
