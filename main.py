from flask import Flask, render_template_string, request

app = Flask(__name__)

# অ্যাডমিন কনফিগারেশন - এখান থেকে সব কন্ট্রোল হবে
config = {
    "task_name": "Watch & Subscribe",
    "task_reward_coins": 15000, # ১৫০০০ কয়েন = ১৫ টাকা
    "tg_link": "#", # এখানে তোমার টেলিগ্রাম লিংক দাও
    "fb_link": "#", # এখানে তোমার ফেসবুক লিংক দাও
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
        :root { --primary: #77e621; --dark: #1a1c24; --nagad: #ed1c24; --gold: #fbbf24; --silver: #cbd5e1; --bronze: #cd7f32; --light: #f4f7f6; }
        body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--light); padding-bottom: 90px; overflow-x: hidden; }
        
        /* Top Navigation */
        .top-nav { background: #2d2f3b; color: white; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 10px rgba(0,0,0,0.2); }
        .coins { background: rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 20px; font-weight: bold; color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3); }

        .page { display: none; padding: 15px; animation: slideIn 0.3s ease; }
        .active { display: block; }
        @keyframes slideIn { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

        /* Fake Withdraw Notification */
        #withdraw-pop { position: fixed; bottom: 85px; left: 50%; transform: translateX(-50%); background: #333; color: white; padding: 10px 20px; border-radius: 30px; font-size: 12px; z-index: 2000; display: none; white-space: nowrap; border: 1px solid var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.3); }

        /* Home Task Cards */
        .task-card { background: white; padding: 20px; border-radius: 20px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #eee; }
        .earn-btn { background: var(--primary); border: none; padding: 10px 20px; border-radius: 20px; font-weight: bold; cursor: pointer; transition: 0.2s; }
        .earn-btn:active { transform: scale(0.95); }

        /* Leaderboard 3D Podiums (image_3.png style) */
        .leaderboard { display: flex; justify-content: center; align-items: flex-end; gap: 15px; margin: 40px 0 20px; }
        .podium { background: white; width: 100px; border-radius: 20px; text-align: center; padding: 15px 10px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); position: relative; }
        .r-1 { height: 160px; border-top: 6px solid var(--gold); order: 2; transform: scale(1.1); z-index: 2; }
        .r-2 { height: 130px; border-top: 6px solid var(--silver); order: 1; }
        .r-3 { height: 110px; border-top: 6px solid var(--bronze); order: 3; }
        .crown { position: absolute; top: -25px; left: 50%; transform: translateX(-50%); color: var(--gold); font-size: 24px; }
        
        /* Gmail Style Profile Pic (MP S) */
        .gmail-profile { width: 55px; height: 55px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 24px; margin: 0 auto 10px; border: 2px solid white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .g-m { background-color: #f44336; } /* M for Maruf */
        .g-p { background-color: #4caf50; } /* P for Pujan? */
        .g-s { background-color: #2196f3; } /* S for Siyam */

        /* Refer Steps (image_4.png style) */
        .refer-steps-container { background: white; padding: 25px; border-radius: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); margin-bottom: 20px; }
        .refer-steps-container h2 { font-size: 18px; margin: 0 0 5px; color: #111; }
        .steps-visual { display: flex; justify-content: space-around; align-items: center; margin: 25px 0 15px; }
        .step-icon { text-align: center; }
        .step-icon i { font-size: 30px; color: var(--primary); display: block; margin-bottom: 5px; }
        .step-icon span { font-size: 12px; font-weight: 600; color: #333; }
        .arrow { color: #eee; font-size: 20px; }
        .step-check { color: #000; font-size: 12px; margin-top: 15px; list-style: none; padding: 0; }
        .step-check li { margin-bottom: 10px; }
        .step-check i { margin-right: 8px; font-size: 16px; }

        /* Refer Button (Below, above navbar) */
        .refer-now-btn { position: fixed; bottom: 75px; left: 50%; transform: translateX(-50%); background: var(--primary); color: #000; border: none; padding: 18px; border-radius: 40px; width: 90%; font-weight: 800; font-size: 18px; box-shadow: 0 8px 25px rgba(119, 230, 33, 0.4); cursor: pointer; z-index: 1000; }

        /* Withdraw Section */
        .w-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .w-card { background: white; padding: 30px 20px; border-radius: 25px; text-align: center; box-shadow: 0 6px 15px rgba(0,0,0,0.03); border: 2px solid transparent; cursor: pointer; transition: 0.2s; }
        .w-card img { width: 70px; margin-bottom: 15px; }
        .w-card.selected { border-color: var(--nagad); background: #fff5f5; box-shadow: 0 6px 20px rgba(237, 28, 36, 0.15); }
        .w-card b { font-size: 22px; color: #000; }
        
        .w-btn-sub { background: var(--dark); color: white; border: none; padding: 18px; border-radius: 40px; width: 100%; font-weight: 800; font-size: 18px; margin-top: 15px; cursor: pointer; }
        .w-btn-hist { background: var(--primary); color: #000; border: none; padding: 15px; border-radius: 30px; width: 100%; font-weight: 800; font-size: 16px; margin-top: 25px; cursor: pointer; box-shadow: 0 4px 15px rgba(119, 230, 33, 0.2); }

        /* Bottom Nav */
        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: white; display: flex; justify-content: space-around; padding: 15px 0; border-top: 1px solid #e5e7eb; z-index: 999; box-shadow: 0 -2px 10px rgba(0,0,0,0.02); }
        .nav-link { text-align: center; color: #9ca3af; font-size: 11px; cursor: pointer; flex: 1; text-decoration: none; font-weight: 600; }
        .nav-link i { font-size: 22px; display: block; margin-bottom: 5px; }
        .active-nav { color: var(--primary); }
    </style>
</head>
<body>

    <div id="withdraw-pop"></div>

    <div class="top-nav">
        <div style="font-weight: 700; font-size: 18px;">EASILY EARNING</div>
        <div class="coins"><i class="fas fa-coins"></i> 81,480 ≈ ৳81.48</div>
    </div>

    <div id="home" class="page active">
        <h3 style="margin-bottom: 20px; margin-left: 5px;">All Tasks</h3>
        
        <div class="task-card">
            <div>
                <b style="font-size: 16px;">Watch & Subscribe 01</b><br>
                <small style="color:var(--primary); font-weight:bold;">Earn 15,000 Coins (৳15)</small>
            </div>
            <button class="earn-btn" onclick="showPage('tasks', 1)">Earn</button>
        </div>

        <div class="task-card">
            <div>
                <b style="font-size: 16px;">YouTube Video Task 02</b><br>
                <small style="color:var(--primary); font-weight:bold;">Earn 15,000 Coins (৳15)</small>
            </div>
            <button class="earn-btn" onclick="showPage('tasks', 1)">Earn</button>
        </div>

        <div class="task-card">
            <div>
                <b style="font-size: 16px;">Complete Video Task 03</b><br>
                <small style="color:var(--primary); font-weight:bold;">Earn 15,000 Coins (৳15)</small>
            </div>
            <button class="earn-btn" onclick="showPage('tasks', 1)">Earn</button>
        </div>
    </div>

    <div id="tasks" class="page">
        <h3>Task Center</h3>
        <div style="background: white; padding: 40px; border-radius: 30px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <i class="fab fa-youtube" style="font-size: 70px; color: #ef4444; margin-bottom: 20px;"></i>
            <p style="font-size: 14px; color: #4b5563;">ভিডিওটি সম্পন্ন করলে আপনি পাবেন ১৫,০০০ কয়েন (৳১৫)।</p>
            <button class="earn-btn" style="padding: 15px; width: 100%; font-size: 16px;" onclick="alert('Task Started!')">Watch Video</button>
        </div>
    </div>

    <div id="refer" class="page" style="padding-bottom: 120px;"> <h3 style="text-align: center; margin-bottom: 5px;">Leaderboard</h3>
        
        <div class="leaderboard">
            <div class="podium r-2">
                <div class="gmail-profile g-p">P</div> <div style="font-size: 12px; font-weight: 700;">Pujan</div>
                <div style="color: var(--nagad); font-size: 11px;">৳4,200</div>
            </div>
            <div class="podium r-1">
                <i class="fas fa-crown crown"></i>
                <div class="gmail-profile g-m">M</div> <div style="font-size: 14px; font-weight: 700;">Maruf</div>
                <div style="color: var(--nagad); font-size: 12px;">৳5,800</div>
            </div>
            <div class="podium r-3">
                <div class="gmail-profile g-s">S</div> <div style="font-size: 12px; font-weight: 700;">Sohag</div>
                <div style="color: var(--nagad); font-size: 11px;">৳3,500</div>
            </div>
        </div>

        <div class="refer-steps-container">
            <h2>Refer Friends & Earn ৳790.00!</h2>
            <div class="steps-visual">
                <div class="step-icon">
                    <i class="fas fa-envelope-open-text"></i>
                    <span>Refer Friends</span>
                </div>
                <i class="fas fa-chevron-right arrow"></i>
                <div class="step-icon">
                    <i class="fas fa-file-contract"></i>
                    <span>Complete 2 Tasks</span>
                </div>
                <i class="fas fa-chevron-right arrow"></i>
                <div class="step-icon">
                    <i class="fas fa-wallet" style="color: var(--gold);"></i>
                    <span>Get ৳10.00</span>
                </div>
            </div>
            <ul class="step-check">
                <li style="color: var(--nagad);"><i class="fas fa-check-circle"></i> Instant Reward: ৳10.00 per friend</li>
                <li style="color: var(--nagad);"><i class="fas fa-check-circle"></i> Ongoing Commission: 10% for friend's additional tasks</li>
                <li style="color: #6b7280; font-size: 11px;"><i class="fas fa-exclamation-triangle"></i> Referred friends must complete 2 tasks to get rewards</li>
            </ul>
        </div>

        <div style="background: white; padding: 20px; border-radius: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); margin-bottom: 20px;">
            <h4 style="margin: 0 0 15px;">Live Payments <small>(৳)</small></h4>
            <div id="live-payouts-list" style="color: #6b7280; font-size: 12px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span>Siyam [Nagad]</span> <b>৳500</b></div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px;"><span>Mursalin [Nagad]</span> <b>৳200</b></div>
                <div style="display: flex; justify-content: space-between;"><span>Abir [Nagad]</span> <b>৳100</b></div>
            </div>
        </div>

        <div style="display: flex; justify-content: center; gap: 30px; margin-top: 25px;">
            <a href="{{ tg_link }}" style="color: #229ED9; font-size: 35px;"><i class="fab fa-telegram-plane"></i></a>
            <a href="{{ fb_link }}" style="color: #1877F2; font-size: 35px;"><i class="fab fa-facebook-f"></i></a>
        </div>

        <button class="refer-now-btn" onclick="alert('Link Copied!')">Refer Now</button>
    </div>

    <div id="withdraw" class="page">
        <h3>Withdraw (Nagad)</h3>
        <div class="w-grid">
            <div class="w-card" onclick="selectW(100, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png" alt="Nagad">
                <b>৳100</b>
            </div>
            <div class="w-card" onclick="selectW(200, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png" alt="Nagad">
                <b>৳200</b>
            </div>
            <div class="w-card" onclick="selectW(300, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png" alt="Nagad">
                <b>৳300</b>
            </div>
            <div class="w-card" onclick="selectW(500, this)">
                <img src="https://download.logo.wine/logo/Nagad/Nagad-Logo.wine.png" alt="Nagad">
                <b>৳500</b>
            </div>
        </div>
        
        <div id="w-form" style="display:none; margin-top:25px; background:white; padding:25px; border-radius:25px; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
            <input type="number" id="phone" placeholder="Enter Nagad Number" style="width: 100%; padding: 18px; border-radius: 15px; border: 1px solid #ddd; outline: none; box-sizing: border-box; font-size: 16px;">
            <button class="w-btn-sub" onclick="alert('Withdraw Request Sent!')">Withdraw Now</button>
        
            <button class="w-btn-hist" onclick="alert('Opening History...')">Withdraw History</button>
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

        function selectW(amt, el) {
            document.querySelectorAll('.w-card').forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
            document.getElementById('w-form').style.display = 'block';
            window.scrollTo(0, document.body.scrollHeight);
        }

        // Fake Withdraw Notifications
        const names = ["Maruf", "Pujan", "Siyam", "Abir", "Mursalin", "Rifat", "Sumon"];
        const amounts = [100, 200, 300, 500];
        
        setInterval(() => {
            const name = names[Math.floor(Math.random() * names.length)];
            const amt = amounts[Math.floor(Math.random() * amounts.length)];
            const pop = document.getElementById('withdraw-pop');
            pop.innerHTML = `<i class="fas fa-check-circle" style="color:var(--primary)"></i> ${name} has withdrawn ৳${amt} to Nagad`;
            pop.style.display = 'block';
            setTimeout(() => { pop.style.display = 'none'; }, 4500);
            
            // Add to live list in refer page
            const list = document.getElementById('live-payouts-list');
            if(list.children.length > 3) list.children[3].remove();
            list.innerHTML = `<div style="display: flex; justify-content: space-between; margin-bottom: 8px; animation: fadeIn 0.5s;"><span>${name} [Nagad]</span> <b>৳${amt}</b></div>` + list.innerHTML;
        }, 8500);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, 
                                  tg_link=config['tg_link'], 
                                  fb_link=config['fb_link'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
