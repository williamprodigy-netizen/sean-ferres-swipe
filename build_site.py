#!/usr/bin/env python3
"""Build the Sean Ferres / Creative Strategist Breakthrough swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build, shell, esc

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/SEAN_FERRES_Swipe")
tx_vsl = sorted(glob.glob(os.path.join(PKG, "Transcript/transcript.md")))

CONFIG = {
    "SITE": "Creative Strategist Breakthrough — Sean Ferres",
    "CREATOR": "Sean Ferres Copy MBA CMB",
    "ADS_KEY": None,
    "FUNNEL_IDS": ["F125"],
    "CAPTURED": "6 & 11 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/SEAN_FERRES_Swipe",
    "BLURB": "The whole business is <b>one page, one form, one call</b>. A 9-minute VSL at "
             "<code>go.seanferres.com</code>, a 60-second Typeform, a Calendly booking. There is "
             "<b>no opt-in, no webinar and no email capture anywhere in the path</b> &mdash; if "
             "you do not apply, he has nothing to follow up with. Behind it sits an ad account "
             "of <b>360 lifetime records where 250 of them are the same piece of copy</b>. The "
             "thing worth stealing is not the funnel. It is the lead: a <b>dated news event</b> "
             "(Meta's Andromeda update) that manufactures urgency off the calendar instead of "
             "off a fake timer.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("board.html", "Wired board"),
        ("pages.html", "Funnel pages"),
        ("ads.html", "Ads"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Program price", "four figures"),
        ("VSL", "9m 13s"),
        ("Objection library", "48m 06s"),
        ("Ad records, lifetime", "360"),
        ("Still live", "39"),
        ("One concept's share", "69%"),
        ("Closer", "Ben Kobamaru"),
        ("Captured", "6 & 11 Aug 2026"),
    ],

    "OFFER": [
        ("Product", "Creative Strategist Breakthrough (CSB / CMB) &mdash; 10-week program"),
        ("Face / operator", "Sean Ferres &mdash; 8 years a copywriter, Australian"),
        ("Entity", "Ferres Enterprises Pty Ltd"),
        ("Big idea", "Meta's <b>Andromeda</b> ad-engine rewrite killed manual targeting and "
                     "created demand for volume, so brands stopped hiring copywriters and "
                     "started hiring <b>creative strategists</b>"),
        ("Promise", "&ldquo;Become a $10K/mo creative strategist in 10 weeks&rdquo;"),
        ("ICP", "Copywriters already earning <b>a few grand a month</b>, or employed with a "
                "stable income. He explicitly disqualifies anyone with no income and anyone "
                "unwilling to commit 10&ndash;12 hours a week."),
        ("Mechanism", "Four parts: <b>reposition</b> as a creative strategist &rarr; "
                      "<b>reverse outreach</b> (target businesses already spending on ads) "
                      "&rarr; <b>inbox AI</b> that gets you onto advertisers' email lists so "
                      "they mail you first &rarr; <b>copy pro</b>, an AI trained on a claimed "
                      "$300M of winning campaigns"),
        ("Guarantee", "Work with you free until you make <b>$5,000 in new income</b> within "
                      "10 weeks"),
        ("The selfish reason", "He says out loud that he runs the program to <b>train people "
                               "he wants to hire or refer</b>, and that graduates may get paid "
                               "to write for his campaigns. A hiring-pipeline frame, not a "
                               "course frame."),
        ("Price", "<b>A one-time four-figure investment.</b> &ldquo;Most students invest a "
                  "few thousand dollars&rdquo;, varying by 1:1 versus group coaching and by "
                  "payment plan. Stated <b>only after you have booked</b>, in FAQ 5 on the "
                  "confirmed page. Software is a separate ~$50/mo, optionally a few hundred."),
        ("Closer", "<b>Ben Kobamaru</b>, head coach &mdash; not Sean. 30-minute "
                   "&ldquo;CMB Gameplan Call&rdquo; on Calendly."),
        ("What CMB stands for", "<b>The Copy Millions Blueprint</b> &mdash; from the confirmed "
                                "page&rsquo;s title tag. Not &ldquo;Copy MBA&rdquo;."),
        ("Entry", "No opt-in. Straight from ad to VSL to a 60-second Typeform."),
        ("Backend", "Calendly &ldquo;game plan call&rdquo;. Tracker present on the Typeform; "
                    "the call page itself was never reached."),
    ],

    "FINDINGS": [
        ("The lead is a dated news event, and that is the one thing worth stealing",
         "He does not open on a promise or a pain. He opens on a <b>calendar fact</b>: Zuck "
         "burned $80bn on the metaverse, redirected the compute into rebuilding the ad engine, "
         "the result is called <b>Andromeda</b>, and it needs volume rather than targeting. "
         "Therefore brands that ran five ads now need 25&ndash;50 per campaign. Therefore a new "
         "role exists and the window to claim it is closing. <b>Urgency comes off the event, "
         "not off a countdown timer.</b> Nothing on the page is scarce; the market is."),
        ("One concept is 69% of everything he has ever run",
         "Of <b>360 lifetime ad records</b>, <b>250</b> carry the same body copy &mdash; "
         "<i>&ldquo;Big clients use your low price as a filter&hellip; to screen you OUT.&rdquo;</i> "
         "It ran January to May 2026 and <b>30 are still live</b>. There are only <b>24 distinct "
         "bodies in the entire history of the account</b>. He does not write new angles; he "
         "re-uploads the winner and lets Andromeda sort out delivery. He is running the playbook "
         "he sells."),
        ("July 2026 added a second layer, and none of it is bundled",
         "Nine new ads went live in July and August, <b>every one a single record</b> with its "
         "own copy: Sam $15k&rarr;$130k in a month, AJ $10k&rarr;$100k in seven months, Akhil "
         "$25k/mo in 60 days, Jack Woods, a sunset walk with Matt Volkwyn, and a Hormozi-adjacent "
         "authority play. <b>All nine are still live.</b> Read against the ladder these are "
         "solution- and product-aware assets sitting on top of one unaware-stage workhorse."),
        ("There is no email capture anywhere before the call",
         "No opt-in page, no lead magnet in the paid path, no newsletter, no phone field. The "
         "captured pages return an <b>empty <code>forms[]</code> array</b>. If a visitor does not "
         "fill the Typeform, he has <b>nothing to follow up with</b> and has to re-buy that person "
         "with retargeting. Both Shelby and Brook capture the email first. "
         "<b>This is the biggest structural weakness in the funnel</b> and it is the one thing "
         "not to copy."),
        ("The Typeform title leaks his naming convention",
         "The application's page title is "
         "<code>CS Breakthrough App Master Funnel v1 - Talking Head</code>. He version-numbers his "
         "funnels and tags them by <b>creative format</b>. &ldquo;Talking Head&rdquo; is the format "
         "this whole master funnel was built around, which lines up with 262 of 360 records being "
         "video. Same class of leak as CreatorHive naming its split test in the "
         "<code>&lt;title&gt;</code> tag."),
        ("The price is four figures, and the refusal to name it is the tactic",
         "There is a 2m48s video called <b>&ldquo;FAQ 5 &mdash; What&rsquo;s the "
         "Investment?&rdquo;</b> sitting on the confirmed page. It says: <b>&ldquo;This is a "
         "one time, four figure investment, not an impulse buy&hellip; most students invest a "
         "few thousand dollars.&rdquo;</b> Then he explains why he will not give one number: "
         "it depends on 1:1 versus group and on payment plan, <i>and</i> &mdash; the real move "
         "&mdash; <i>&ldquo;we do raise the price every so often&hellip; the price only moves in "
         "one direction and that is up. So whatever the investment is now will be the lowest "
         "it&rsquo;ll ever be.&rdquo;</i> <b>He converts the absence of a price into a scarcity "
         "argument.</b> Software is broken out separately at ~$50/mo, with an optional "
         "&ldquo;AI outreach machine&rdquo; at a couple hundred more."),
        ("The confirmed page is a 48-minute objection library and it is the best asset here",
         "Fourteen Wistia videos, <b>48m06s total</b>, one per objection: what is Reverse "
         "Outreach, what does a creative strategist actually do, will this work if I&rsquo;m a "
         "beginner, how much time, how long until I make money, how is this different, "
         "I&rsquo;m not good with tech, what countries, why now, and what&rsquo;s the "
         "investment. Plus a 9m55s pre-call video, a client logo wall (Hormozi, Robbins, "
         "Bet-David, Graziosi, Brunson, Kennedy, Martell, Belfort) and named testimonials. "
         "<b>This is the Brook Hiddink pre-call-workshop pattern</b>, and it is the single "
         "most copyable thing in the funnel."),
        ("His own file names date the repositioning to mid-May 2026",
         "Wistia's JSON-LD tags every video with the funnel that commissioned it. Nine are "
         "<code>HAMMER THEM FUNNEL 2.0 - COPYWRITERS 2026</code>, uploaded 23 Feb. Five are "
         "<code>HAMMER THEM FUNNEL 3.0 - CS BREAKTHROUGH</code>, uploaded 14&ndash;16 May. "
         "<b>That is the same month as the ad cohort that is still 100% alive.</b> The pivot, "
         "the new creative and the surviving ads are one event, and we can date it to the week."),
        ("The confirmed page still runs the OLD videos, and they contradict the new pitch",
         '<span class="tag warn">CAUTION</span> Nine of the fourteen are 2.0-era. The '
         'investment FAQ a freshly-booked lead watches still says the goal is '
         '<b>&ldquo;$10,000 a month <i>as a copywriter</i>&rdquo;</b> and calls the program the '
         '&ldquo;CMB breakthrough challenge&rdquo;. Ben&rsquo;s Calendly page sells '
         '&ldquo;$5k&ndash;10k/mo as an <b>AI-powered copywriter</b>&hellip; Reverse Outreach + '
         'AI&rdquo;. The ad and the VSL sell &ldquo;creative strategist&rdquo;. '
         '<b>The Andromeda repositioning is a front-end layer over a product that has not '
         'finished moving.</b> A prospect who watches everything gets three different offer '
         'names in one funnel.'),
        ("Applying enrols you in a live training that appears nowhere else",
         '<span class="tag warn">UNVERIFIED</span> The DQ ending reads: &ldquo;the '
         '<b>Creative Strategist 101</b> free live training <b>you just signed up for</b>&rdquo;. '
         'So the application silently registers you for a training that is not mentioned on the '
         'VSL page, in any ad, or on any captured step. We could not locate a page for it. '
         'If it is real, the &ldquo;no webinar&rdquo; read on this funnel is incomplete.'),
        ("The confirmed page throws away everything Calendly hands it",
         "Calendly redirects with <code>assigned_to</code>, <code>event_type_name</code>, "
         "<code>event_start_time</code>, <code>invitee_full_name</code> and "
         "<code>text_reminder_number</code> in the query string. The page reads <b>none</b> of "
         "them &mdash; no <code>URLSearchParams</code>, no personalisation, no name, no "
         "rendered appointment time. For a four-figure offer that is a free trust beat left on "
         "the floor."),
        ("He rebuilt the offer, not just the creative",
         "Everything from 2025 is switched off. The <b>Copy MBA</b> page (108248635378423) is "
         "running <b>zero ads</b>. The AI-copywriting positioning &mdash; <i>&ldquo;Crypto's "
         "window closed. AI is the next gold rush&rdquo;</i>, the robot-chef ad, the Bigfoot "
         "AI-video ad, the <code>freecopyclass.com</code> live webinar and the "
         "<code>copymba.com</code> VSL &mdash; is <b>100% dead across ~100 records and 13 "
         "concepts</b>. He moved the ads to a plain-name page (&ldquo;Sean Ferres&rdquo;, "
         "438598856674850) and changed mechanism from webinar to VSL-plus-application."),
        ("The guarantee does the work the price cannot",
         "With no price on the page, the risk-reversal has to carry the whole close: "
         "<b>&ldquo;we'll keep working with you for free until you make at least $5,000 in new "
         "income&rdquo;</b>. It is scoped to a number, not a refund, and it is conditional on "
         "implementation. Cheaper for him than a money-back guarantee and it reads stronger."),
        ("He names his own selfish motive on purpose",
         "A full 45 seconds of a 9-minute VSL is spent explaining that he runs the program to "
         "<b>train people he wants to hire or refer</b>, and that good graduates get paid to "
         "write for his campaigns and for his network. It converts the offer from &ldquo;buy my "
         "course&rdquo; into &ldquo;join my hiring pipeline&rdquo;, and it pre-empts the "
         "&ldquo;why are you teaching this instead of doing it&rdquo; objection before it forms."),
        ("Proof is a ladder, deliberately, with the top rung disclaimed",
         "He gives three tiers and labels them: Sam at <b>$49k from one client then $78k the next "
         "month</b> (extreme), AJ at <b>$1k &rarr; $10k/mo</b> (&ldquo;here's what typical looks "
         "like&rdquo;), and Charney at <b>one $2k/mo retainer</b> (&ldquo;on the other end of the "
         "spectrum&rdquo;). He then explicitly says <i>&ldquo;I'm absolutely not saying you're "
         "gonna come in here and start making seven figures&rdquo;</i>. The disclaimer buys "
         "credibility for the mid-tier number, which is the one he actually wants believed."),
        ("The whole application, and its gate, are published in the page source",
         "Typeform ships the entire form model in the HTML. Form <code>AhJWFsEs</code>, "
         "<b>9 fields, 3 endings</b>, nothing submitted. The questions: experience level, "
         "90-day goal, hours per week, <b>current monthly income</b>, contact info, why now "
         "(long text), <b>what you could invest in the next 14 days</b> "
         "(under $500 / $500&ndash;2k / $2k&ndash;4k / $4k+), phone number, then the Calendly "
         "block. <b>The DQ rule is a single OR:</b> hours = under 7/week, <b>OR</b> budget = "
         "under $500, <b>OR</b> experience = &ldquo;what&rsquo;s copywriting?&rdquo;. "
         "Everything else is <code>always &rarr; Pre-Approved</code>. "
         "<b>Income is collected but does not gate</b> &mdash; you can earn under $3k/mo and "
         "still reach the call. The phone number is captured at Q8, <b>before</b> the DQ fires."),
        ("The DQ path is a downsell, not a door",
         "Fail and you do not get a dead end. You get: <i>&ldquo;CMB isn&rsquo;t the right fit "
         "yet. Our coaching is designed for ambitious copywriters who can invest at least 10 "
         "hours a week and <b>a few thousand dollars</b>&hellip;&rdquo;</i> plus a YouTube "
         "crash course and a push into the free live training. The rejection copy is also "
         "<b>the only place the price appears before booking</b> &mdash; he tells you what it "
         "costs at the exact moment he tells you that you cannot have it."),
        ("What is still missing",
         '<span class="tag bad">GAP</span> The email and SMS sequences (Will booked with a real '
         'address on 11 Aug, so these should start arriving). The &ldquo;Creative Strategist '
         '101&rdquo; training page. The product itself. The brand site&rsquo;s cheat-sheet lead '
         'magnet still returns <b>403</b>. Everything else in this funnel is now captured.'),
    ],

    "FUNNEL": [
        ("Meta ad", "facebook.com/ads/library &mdash; page 438598856674850",
         "39 live records. 262 of 360 lifetime are video. Every live one points at the VSL."),
        ("VSL page", "go.seanferres.com",
         "9m13s Wistia VSL, then a very long proof scroll with 20+ YouTube testimonial embeds. "
         "Trackers: <b>Wistia + Typeform + GoHighLevel</b>. "
         '<span class="tag bad">no email capture</span>'),
        ("Application", "seanferres.typeform.com/CSB-master-1",
         'Typeform, 60 seconds, &ldquo;See If You Qualify&rdquo;. Carries a <b>Calendly</b> '
         'tracker. <span class="tag warn">only Q1 and Q2 observed</span>'),
        ("Game plan call", "calendly.com/coachbenc/cmb-gameplan-call",
         '<b>Ben Kobamaru</b>, 30 min. Publicly bookable without applying. Copy here sells '
         '&ldquo;$5k&ndash;10k/mo as an <b>AI-powered copywriter</b>&hellip; Reverse Outreach '
         '+ AI&rdquo; &mdash; a different offer than the ad. '
         '<span class="tag good">booked 11 Aug</span>'),
        ("Confirmed page", "go.seanferres.com/confirmed",
         '&ldquo;Call Booked | <b>The Copy Millions Blueprint</b>&rdquo;. 9m55s pre-call video, '
         '<b>14-video / 48m06s objection library</b>, client logo wall, testimonials. Ignores '
         'every Calendly parameter. Trackers: Meta, GTM, GA, <b>TikTok</b>, Clarity, GHL, Wistia.'),
        ("Brand site", "seanferres.com",
         "Ferres Enterprises Pty Ltd. Testimonial wall, press logos, one CTA to a free cheat "
         "sheet. <b>The ads never point here.</b>"),
        ("Lead magnet", "seanferres.com/cheat-sheet",
         '<span class="tag bad">403</span> &mdash; blocked to this environment, never captured.'),
        ("Copy MBA page (dead)", "facebook.com/ads/library &mdash; page 108248635378423",
         '<span class="tag bad">zero active ads</span> &mdash; the 2025 brand, switched off.'),
    ],

    "TRANSCRIPT_GROUPS": [
        ("VSL — Creative Strategist Breakthrough, 9m 13s, 2,212 words", tx_vsl),
    ],

    "SLIDE_PAGES": [],
    "DECKS": [],

    "VIDEOS": [
        ("FAQ 5 — What's the Investment? (Wistia jd8dy1941f)", 168, "36 MB",
         "<b>The price answer.</b> &ldquo;A one time, four figure investment&hellip; most "
         "students invest a few thousand dollars.&rdquo; Pulled and transcribed &mdash; see "
         "<code>03_TRANSCRIPTS/Sean Ferres/FAQ5_whats_the_investment.md</code>. Tagged "
         "<code>HAMMER THEM FUNNEL 2.0</code>, so a booked lead watches the old positioning."),
        ("Confirmed-page pre-call video (Wistia 5mm3lxvfq8)", 595, "&mdash;",
         "&ldquo;CS Book a Call Confirmation Page Vid&rdquo;, uploaded 14 May 2026. Tagged "
         "<code>HAMMER THEM FUNNEL 3.0 - CS BREAKTHROUGH</code> &mdash; the newest asset in "
         "the funnel. Not downloaded."),
        ("Objection library — 12 further FAQ videos", 2124, "&mdash;",
         "48m06s total across 14 videos. Nine tagged FUNNEL 2.0 (Feb 2026), five tagged "
         "FUNNEL 3.0 (May 2026). Full inventory with Wistia ids in "
         "<code>02_Pages/06_Confirmed_booked/video_inventory.json</code>."),
        ("source.mp4", 553, "222 MB",
         "The 9m13s VSL from <code>go.seanferres.com</code>. Wistia, 1920&times;1080, pulled at "
         "native quality. <b>VSL rule applied</b> &mdash; source video and transcript only, no "
         "slide extraction and no deck."),
    ],

    "EMAIL_NOTE": "A call was booked on 11 August 2026 against the research address, so the "
                  "post-booking email and SMS layers should now start arriving and will be "
                  "picked up by the daily sweep. Note the funnel captures a phone number at "
                  "application Q8 and a second text-reminder number at Calendly, so expect SMS "
                  "as well as email. Nothing had arrived at time of writing.",

    "ANALYSIS": """
<div class="note"><b>The one-line read.</b> Ferres runs the <b>simplest funnel in this entire
swipe file</b> &mdash; ad, VSL, form, call &mdash; and spends all his leverage on the
<b>lead</b> instead. The Andromeda news event does the work a webinar, an opt-in sequence and a
countdown timer would normally have to do. That is a trade worth understanding before copying
either half of it.</div>

<h2 class="sec">The news-event lead, taken apart</h2>
<p>This is the structure, stripped of his specifics. Every step is a fact the reader can check,
which is what stops it reading as hype:</p>
<div class="tablewrap"><table>
<tr><th>Beat</th><th>What it does</th><th>His version</th></tr>
<tr><td><b>1. The event</b></td><td>An external, dated, verifiable thing happened</td>
<td>Meta rebuilt its ad engine. It is called Andromeda.</td></tr>
<tr><td><b>2. The mechanism</b></td><td>Why the event changes the economics</td>
<td>It no longer needs manual targeting. It needs volume.</td></tr>
<tr><td><b>3. The consequence</b></td><td>A concrete, countable new demand</td>
<td>Brands that ran 5 ads now need 25&ndash;50 creatives per campaign.</td></tr>
<tr><td><b>4. The vacancy</b></td><td>Who the market must now pay, and what they are called</td>
<td>Nobody in-house can do it. The role is &ldquo;creative strategist&rdquo;.</td></tr>
<tr><td><b>5. The closing window</b></td><td>Urgency off the calendar, not off a timer</td>
<td>&ldquo;Over the next 30&ndash;90 days a wave of brands all pick their person and settle in
for 12+ months.&rdquo;</td></tr>
</table></div>
<p>Step 5 is the one most people get wrong. He never says &ldquo;this offer closes Friday&rdquo;.
He says the <b>market</b> closes, and puts a plausible horizon on it. Nothing to disprove, nothing
to expire, and it survives the ad running for eight straight months.</p>

<div class="note"><b>Where this points harder at UGC World than at him.</b> The same event is a
stronger argument for us. Fifty videos a month is a <b>filming</b> problem before it is a writing
problem &mdash; a marketing department cannot produce that volume in-house at any price, and a
studio is too slow. His version needs the reader to accept that copywriting is being repriced.
Ours only needs them to accept that someone has to hold the camera. That work is already drafted
in the Copy SSOT inbox as the Andromeda news-event ad.</div>

<h2 class="sec">The ad account, age-controlled</h2>
<p>Raw survival counts would say his January&ndash;March work was a disaster and his summer work
is perfect. That is mostly age. What is <i>not</i> age is the May cohort:</p>
<div class="tablewrap"><table>
<tr><th>Cohort</th><th>Records</th><th>Still live</th><th>Read</th></tr>
<tr><td>Nov 2024 &ndash; Oct 2025</td><td>~100</td><td><b>0</b></td>
<td>The Copy MBA / AI-copywriting era. Dead as a positioning, not just as creative.</td></tr>
<tr><td>Jan &ndash; Mar 2026</td><td>215</td><td><b>0</b></td>
<td>The workhorse concept at full bundle volume. Retired, but the concept was not.</td></tr>
<tr><td>May 2026</td><td>28</td><td><b>28</b></td>
<td>Same copy, re-uploaded. <b>100% survival at three months old</b> &mdash; this is the
proof the concept is a winner, not the raw record count.</td></tr>
<tr><td>Jul &ndash; Aug 2026</td><td>9</td><td><b>9</b></td>
<td>The unbundled proof layer. Too young to read as survival; read it as a deliberate
second lane.</td></tr>
</table></div>
<p class="small">n = 360 records parsed from the public Ad Library graphql stream on 11 Aug 2026.
Records, not unique creatives &mdash; Meta counts a re-upload as a new record, which is exactly
what makes the bundle ratio measurable.</p>

<h2 class="sec">What to take, and what to leave</h2>
<div class="tablewrap"><table>
<tr><th>&nbsp;</th><th>Element</th><th>Why</th></tr>
<tr><td><span class="tag good">TAKE</span></td><td>The news-event lead structure</td>
<td>Urgency that does not decay and cannot be disproved. Already drafted for us.</td></tr>
<tr><td><span class="tag good">TAKE</span></td><td>Naming the selfish reason out loud</td>
<td>Converts &ldquo;buy my course&rdquo; into &ldquo;join my pipeline&rdquo; and kills the
why-are-you-teaching-this objection before it forms. We have a stronger version of this claim
than he does, because the placements are real.</td></tr>
<tr><td><span class="tag good">TAKE</span></td><td>The disclaimed proof ladder</td>
<td>Extreme / typical / floor, with the extreme explicitly disclaimed. Buys belief for the
middle number, which is the one that sells.</td></tr>
<tr><td><span class="tag good">TAKE</span></td><td>Scoped guarantee to a dollar figure</td>
<td>&ldquo;Free until you make $5,000&rdquo; is cheaper than a refund and reads stronger.</td></tr>
<tr><td><span class="tag warn">WATCH</span></td><td>One concept, 250 uploads</td>
<td>Correct for Andromeda, but it means a single point of failure. When that concept fatigues
he has 23 other bodies in eight months of history to fall back on.</td></tr>
<tr><td><span class="tag bad">LEAVE</span></td><td>No email capture before the call</td>
<td>Every non-applicant is lost and must be re-bought. Our funnel captures at registration and
should keep doing so.</td></tr>
<tr><td><span class="tag good">TAKE</span></td><td>The 48-minute objection library on the
confirmed page</td>
<td>One video per objection, watched between booking and the call. Same pattern as Brook's
pre-call workshop. This is the highest-leverage thing on this site and we do not have an
equivalent.</td></tr>
<tr><td><span class="tag good">TAKE</span></td><td>&ldquo;The price only moves up, so today is
the lowest it will ever be&rdquo;</td>
<td>Turns refusing to name a price into a reason to act now. Costs nothing and it is true of
most programs.</td></tr>
<tr><td><span class="tag bad">LEAVE</span></td><td>Three offer names in one funnel</td>
<td>Ad says creative strategist, Calendly says AI-powered copywriter, confirmed page says Copy
Millions Blueprint, and the investment video says &ldquo;$10k/mo as a copywriter&rdquo;. A
prospect who watches everything gets four different products. Pick one name and hold it.</td></tr>
<tr><td><span class="tag bad">LEAVE</span></td><td>The unsourced volume claim</td>
<td>&ldquo;25&ndash;50 creatives per campaign&rdquo; is <b>his</b> number, repeated without a
source. If we run the same event we source it or soften it to &ldquo;dozens&rdquo;.</td></tr>
</table></div>

<h2 class="sec">He version-numbers everything, and it all leaks</h2>
<p>Two independent naming leaks, both in metadata he did not think anyone would read:</p>
<div class="tablewrap"><table>
<tr><th>Where</th><th>What it says</th><th>What it tells you</th></tr>
<tr><td>Typeform page title</td><td><code>CS Breakthrough App Master Funnel v1 - Talking Head</code></td>
<td>He versions his funnels and tags them by <b>creative format</b>. &ldquo;Talking Head&rdquo;
matches 262 of 360 records being video.</td></tr>
<tr><td>Wistia JSON-LD, &times;9</td><td><code>HAMMER THEM FUNNEL 2.0 - COPYWRITERS 2026</code></td>
<td>The Feb 2026 build. The AI-copywriter era.</td></tr>
<tr><td>Wistia JSON-LD, &times;5</td><td><code>HAMMER THEM FUNNEL 3.0 - CS BREAKTHROUGH</code></td>
<td>Uploaded 14&ndash;16 May 2026. <b>Dates the pivot to the week</b>, and it is the same month
as the ad cohort that is still 100% alive.</td></tr>
</table></div>
<p>Worth internalising as a habit: <b>check the title tag and the video schema on every funnel
you swipe.</b> CreatorHive named its split test in the <code>&lt;title&gt;</code>; Ferres named
his whole roadmap in his video metadata. Neither cost anything to find.</p>

<h2 class="sec">Open questions</h2>
<ul>
<li>What is the &ldquo;Creative Strategist 101&rdquo; free live training that the DQ ending says
you were auto-enrolled in? No page for it exists on any captured step.</li>
<li>What does the post-booking email and SMS sequence actually do? A call is booked as of
11 Aug, so this should answer itself within days.</li>
<li>Where exactly does the four-figure number land &mdash; the Q7 bands imply the real spread is
<b>$2k&ndash;4k for group and $4k+ for 1:1</b>, but that is inference, not evidence.</li>
<li>Does he run TikTok? A TikTok pixel fires on the confirmed page but every ad we found is Meta.</li>
</ul>
""",
}


def page_ads(cfg):
    """The ad-account teardown. Built here rather than by the shared builder
    because gethookd has no usable brand record for him — every number on this
    page came out of the public Ad Library graphql stream."""
    import json, datetime, collections
    src = os.path.expanduser(
        "~/UNDERGROUND_FUNNELS_SSOT/01_RAW_FUNNELS/Sean_Ferres_Copy_MBA_CMB - "
        "Creative_Strategist_Breakthrough_-_10-week_program - 2026-08-06/12_Ads/"
        "ferres_page_all__ads_clean.json")
    ads = json.load(open(src))
    for a in ads:
        a["m"] = (datetime.date.fromtimestamp(int(a["start_date"])).strftime("%Y-%m")
                  if a.get("start_date") else "?")
        a["concept"] = (a.get("body") or "").strip().replace("\n", " ")

    groups = collections.defaultdict(list)
    for a in ads:
        groups[a["concept"][:70]].append(a)
    ordered = sorted(groups.items(), key=lambda kv: -len(kv[1]))

    rows = []
    for key, v in ordered:
        live = sum(1 for a in v if a["is_active"])
        months = sorted({a["m"] for a in v if a["m"] != "?"})
        span = months[0] if len(months) == 1 else f"{months[0]} &rarr; {months[-1]}"
        # span already carries an HTML entity — must not go through esc()
        body = v[0]["concept"]
        if body.startswith("{{"):
            body = ("\u2014 dynamic-creative template, body pulled from the product feed "
                    "at delivery. Meta stores the unrendered variable, so the copy these "
                    "actually served is not recoverable from the library.")
        tag = ('<span class="tag good">live</span>' if live else
               '<span class="tag bad">dead</span>')
        rows.append(
            f"<tr><td>{tag}</td><td><b>{len(v)}</b></td><td><b>{live}</b></td>"
            f"<td class='small'>{span}</td>"
            f"<td>{esc(body[:230])}{'&hellip;' if len(body) > 230 else ''}</td></tr>")

    cohorts = collections.defaultdict(lambda: [0, 0])
    for a in ads:
        c = cohorts[a["m"]]
        c[0] += 1
        c[1] += 1 if a["is_active"] else 0
    crows = "".join(
        f"<tr><td>{esc(m)}</td><td>{t}</td><td>{l}</td>"
        f"<td>{'&mdash;' if not t else f'{l * 100 // t}%'}</td></tr>"
        for m, (t, l) in sorted(cohorts.items()))

    fmt = collections.Counter(a.get("display_format") or "?" for a in ads)
    frows = "".join(f"<tr><td>{esc(k)}</td><td>{v}</td></tr>"
                    for k, v in fmt.most_common())

    total, live_n = len(ads), sum(1 for a in ads if a["is_active"])
    return shell(cfg, "ads.html", "Ads", f"""
<div class="hero"><div class="kick">{total} lifetime records &middot; {live_n} live</div>
<h1>The ad account</h1>
<p>Parsed out of the public Meta Ad Library graphql stream on 11 August 2026, from the
<b>Sean Ferres</b> advertiser page (<code>438598856674850</code>). The older
<b>Copy MBA</b> page (<code>108248635378423</code>) is running <b>zero</b> ads.
gethookd has no usable brand record for him, so nothing here comes from a paid tool.</p></div>

<section><div class="note"><b>Records, not creatives.</b> Meta counts a re-upload as a new
record. That is what makes the bundling measurable: <b>{total} records</b> across the whole
history of the account resolve to only <b>{len(ordered)} distinct bodies of copy</b>.</div></section>

<section><h2 class="sec">Every concept he has ever run</h2>
<div class="tablewrap"><table>
<tr><th>&nbsp;</th><th>Records</th><th>Live</th><th>Ran</th><th>Opening copy</th></tr>
{"".join(rows)}</table></div></section>

<section><h2 class="sec">By launch month</h2>
<p>Survival has to be read within a cohort or age fakes the finding. The row that matters is
<b>May 2026 at 100%</b> &mdash; same copy as the dead January&ndash;March records, three months
old, and every one still running.</p>
<div class="tablewrap"><table>
<tr><th>Month</th><th>Records</th><th>Still live</th><th>Survival</th></tr>
{crows}</table></div></section>

<section><h2 class="sec">Format mix</h2>
<div class="tablewrap"><table><tr><th>Format</th><th>Records</th></tr>{frows}</table></div>
<p class="small">Lines up with the Typeform title, which calls the whole build
<code>CS Breakthrough App Master Funnel v1 - <b>Talking Head</b></code>.</p></section>""")


if __name__ == "__main__":
    build(CONFIG)
    open(os.path.join(REPO, "ads.html"), "w").write(page_ads(CONFIG))
    print("  ads.html")
    build(CONFIG)          # rebuild so every nav picks ads.html up
