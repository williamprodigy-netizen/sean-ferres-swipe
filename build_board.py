#!/usr/bin/env python3
"""Sean Ferres / Copy MBA — whole-business wired board.

One pannable canvas. Every funnel step is the real screenshot, wired together.

The story the board has to tell: he runs ONE workhorse cold concept, bundled
250 times, into a single 9-minute VSL and a 60-second Typeform. Everything he
built in 2025 under the Copy MBA brand is dead. In July 2026 he layered a
second, unbundled lane of proof/story ads on top of the same VSL.

Layout rule: one column per funnel STEP. Parallel variants stack vertically
inside that column, so an arrow never crosses a card it is not pointing at.

Run:  python3 build_board.py   ->  board.html
"""
import base64, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DIMS = json.load(open(os.path.join(HERE, "dims.json")))
SHOTS_SRC = os.path.join(HERE, "media", "full")

CARD_W = 330
CHROME = 166
X = {1: 60, 2: 560, 3: 1060, 4: 1560, 5: 2060, 6: 2560}

LANE_TAG = {"live": "LIVE FUNNEL", "dead": "DEAD — 2025 ERA", "proof": "PROOF LAYER"}
PAID, DEAD, PROOF = "#818cf8", "#64748b", "#34d399"

# id -> (asset, col, y, lane, title, url, note)
SHOTS = {
    "vsl": ("ferres_01_VSL", 2, 150, "live", "The VSL page",
            "https://go.seanferres.com/",
            "One page carries the whole business. 9-minute Wistia VSL at the top, "
            "then a very long proof scroll. No opt-in, no email capture, no "
            "webinar. Trackers: Wistia + Typeform + GoHighLevel."),
    "app": ("ferres_03_Application", 3, 150, "live", "60-second application",
            "https://seanferres.typeform.com/CSB-master-1",
            "Typeform, not a booking page. Title leaks the naming convention: "
            "&ldquo;CS Breakthrough App Master Funnel v1 - Talking Head&rdquo;. "
            "Carries a Calendly tracker, so the call sits behind it."),
    "cal": ("ferres_05_Calendly", 4, 150, "live", "The booking page",
            "https://calendly.com/coachbenc/cmb-gameplan-call",
            "<b>Ben Kobamaru</b>, not Sean. 30-minute &ldquo;CMB Gameplan Call&rdquo;. "
            "The copy here still sells the <b>old</b> offer: &ldquo;$5k&ndash;10k/mo as an "
            "<b>AI-powered copywriter</b>&hellip; Reverse Outreach + AI&rdquo;."),
    "confirmed": ("ferres_06_Confirmed", 5, 150, "live", "Confirmed page",
                  "https://go.seanferres.com/confirmed",
                  "Titled <b>&ldquo;Call Booked | The Copy Millions Blueprint&rdquo;</b>. "
                  "A 9m55s pre-call video plus a <b>numbered objection library of 14 Wistia "
                  "videos, 48m06s total</b>, a client logo wall and named testimonials. "
                  "<b>The most copyable asset in the funnel.</b> It ignores every Calendly "
                  "parameter &mdash; no name, no appointment time rendered."),
    "brand": ("ferres_02_Brand_site", 6, 780, "dead", "Brand site (side door)",
              "https://seanferres.com/",
              "Ferres Enterprises Pty Ltd, Australian entity. Testimonial wall "
              "and one CTA to a free cheat sheet. Not where the ads point."),
    "ads": ("ferres_04_Ad_library", 1, 150, "live", "Meta Ad Library — live",
            "https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
            "&country=ALL&view_all_page_id=438598856674850",
            "The advertiser page is &ldquo;Sean Ferres&rdquo; (438598856674850). "
            "The old &ldquo;Copy MBA&rdquo; page (108248635378423) is running zero ads."),
}

# id -> (col, y, h, lane, kicker, title, rows[], foot)
DATA = {
    "concept": (1, 1400, 430, "live", "THE WORKHORSE", "One concept, 250 uploads",
                [("Records", "250"), ("Still live", "30"),
                 ("Ran", "Jan &rarr; May 2026"), ("Share of all history", "69%"),
                 ("Distinct bodies, all-time", "24")],
                "&ldquo;Big clients use your low price as a filter&hellip; to screen "
                "you OUT.&rdquo; One piece of copy, re-uploaded 250 times. Textbook "
                "Andromeda bundling."),
    "julywave": (2, 1400, 470, "proof", "JULY 2026 — NEW LAYER", "9 proof ads, zero bundling",
                 [("Records", "9"), ("Still live", "9"), ("Bundled", "none — 1 each"),
                  ("Format", "8 video, 1 image"), ("Lands on", "the same VSL")],
                 "Every one is a named student story: Sam $15k&rarr;$130k, AJ "
                 "$10k&rarr;$100k, Akhil $25k in 60 days, Jack Woods, plus a "
                 "Hormozi-adjacent authority play. Solution- and product-aware."),
    "dead2025": (3, 1400, 470, "dead", "THE 2025 ERA — ALL DEAD", "Copy MBA / AI copywriting",
                 [("Concepts", "13"), ("Records", "~100"), ("Still live", "0"),
                  ("Pages", "copymba.com, freecopyclass.com"),
                  ("Mechanism", "live webinar, then a VSL")],
                 "&ldquo;Crypto&rsquo;s window closed. AI is the next gold rush.&rdquo; "
                 "The whole AI-copywriter positioning, plus the webinar funnel, is "
                 "switched off. He rebuilt the offer, not just the creative."),
    "objlib": (5, 780, 500, "live", "THE COPYABLE ASSET", "Objection library, 48m06s",
               [("Videos", "14"), ("Total runtime", "48m 06s"),
                ("Tagged FUNNEL 2.0", "9 &mdash; Feb 2026"),
                ("Tagged FUNNEL 3.0", "5 &mdash; May 2026"),
                ("Personalisation", "none")],
               "Every objection gets its own video: investment, beginner, tech, time, "
               "countries, how-is-this-different, why-now. Wistia metadata tags each one "
               "with his internal funnel version, which is how we dated the pivot."),
    "app_detail": (3, 780, 470, "live", "READ FROM THE PUBLIC FORM", "All 9 questions, and the gate",
                   [("Form id", "AhJWFsEs"), ("Fields", "9"),
                    ("Money question", "Q7, four bands"),
                    ("Phone captured", "Q8 &mdash; before the DQ"),
                    ("Endings", "3")],
                   "Nothing was submitted. Typeform publishes the entire form model, "
                   "logic and endings in the page source."),
    "offer": (6, 150, 470, "live", "THE OFFER", "Creative Strategist Breakthrough",
              [("Length", "10 weeks"), ("Promise", "$10k/mo creative strategist"),
               ("Guarantee", "work free until you make $5,000"),
               ("Price", "four figures, one-time"),
               ("Entity", "Ferres Enterprises Pty Ltd")],
              "Reverse outreach system, an inbox AI that gets you onto advertisers&rsquo; "
              "email lists, and &ldquo;copy pro&rdquo; trained on a claimed $300M of "
              "winning campaigns."),
}

# ---------------------------------------------------------------- routing logic
# (id, x, y, state, condition, body, evidence)
BRANCH = [
    ("b_news", X[1] + 15, 2020, "yes", "The lead is a dated news event",
     "The hook is not a promise, it is a <b>calendar fact</b>. Meta rebuilt its ad "
     "engine (Andromeda), it stopped needing manual targeting, so it needs volume, "
     "so brands need 25-50 creatives per campaign. Urgency comes off the event, not "
     "off a fake timer. <b>This is the one thing worth stealing.</b>",
     "VERIFIED &middot; VSL transcript 00:00:00&ndash;00:01:32, 2,212 words"),
    ("b_bundle", X[2] + 15, 2020, "yes", "One concept carries the account",
     "250 of 360 lifetime ad records are the same body copy. He does not write new "
     "angles, he <b>re-uploads the winner</b> and lets Andromeda sort it out. Only "
     "<b>24 distinct bodies</b> exist in the whole history of the account.",
     "VERIFIED &middot; 360 ad records parsed from the public Ad Library graphql"),
    ("b_dq", X[3] + 15, 2020, "dq", "Three ways to fail, and only three",
     "The form jumps to the DQ ending if <b>ANY</b> of: hours = "
     "&ldquo;under 7 a week&rdquo; <b>OR</b> budget = &ldquo;under $500&rdquo; <b>OR</b> "
     "experience = &ldquo;what&rsquo;s copywriting?&rdquo;. Everything else is "
     "<code>always &rarr; Pre-Approved</code>. <b>Income does not gate.</b> You can "
     "earn under $3k/mo and still reach the call.",
     "VERIFIED &middot; read from the form&rsquo;s public logic block, nothing submitted"),
    ("b_price", X[4] + 15, 2020, "yes", "The price, and why he refuses to say it",
     "<b>A one-time four-figure investment. &ldquo;Most students invest a few thousand "
     "dollars.&rdquo;</b> He says it on camera and then explains the refusal: it varies by "
     "1:1 versus group, and <i>&ldquo;we raise the price every so often&hellip; the price "
     "only moves in one direction and that is up, so whatever the investment is now will "
     "be the lowest it&rsquo;ll ever be.&rdquo;</i> <b>The refusal is the tactic</b> &mdash; "
     "it converts &ldquo;no price&rdquo; into a scarcity argument.",
     "VERIFIED &middot; FAQ 5 transcript, Wistia jd8dy1941f, 2m48s, pulled and transcribed"),
    ("b_backend", X[5] + 15, 2020, "dq", "The pivot is dated to mid-May 2026, by his own file names",
     "Wistia tags every video with the funnel that commissioned it. Nine are "
     "<code>HAMMER THEM FUNNEL 2.0 - COPYWRITERS 2026</code> (Feb). Five are "
     "<code>HAMMER THEM FUNNEL 3.0 - CS BREAKTHROUGH</code> (14&ndash;16 May). "
     "<b>The confirmed page still runs a mix of both</b>, so the investment FAQ a booked "
     "lead watches is the old one, still saying &ldquo;$10,000 a month <b>as a "
     "copywriter</b>&rdquo;. <b>That is the same month the surviving ad cohort launched.</b>",
     "VERIFIED &middot; Wistia JSON-LD upload dates + funnel tags on all 14 videos"),
    ("b_training", X[6] + 15, 2020, "unver", "There is a free live training we never found",
     "The DQ ending says: &ldquo;the <b>Creative Strategist 101</b> free live training "
     "<b>you just signed up for</b>&rdquo;. So applying enrols you in a training that "
     "appears nowhere on the VSL page, in the ads, or in any captured step.",
     "UNVERIFIED &middot; their claim, in their own form copy. No page for it located."),
]


def branch_card(b):
    bid, x, y, state, cond, body, ev = b
    cls = "br " + ("unver" if "UNVERIFIED" in ev or "PARTIALLY" in ev else state)
    return (f'<div class="{cls}" style="left:{x}px;top:{y}px">'
            f'<span class="cond">{cond}</span><p>{body}</p>'
            f'<span class="ev">{ev}</span></div>')


A = []


def b64(rel):
    p = os.path.join(SHOTS_SRC, os.path.basename(rel).replace(".jpg", ".jpg"))
    with open(p, "rb") as fh:
        return "data:image/jpeg;base64," + base64.b64encode(fh.read()).decode()


def node_box(nid):
    if nid in SHOTS:
        asset, col, y = SHOTS[nid][0], SHOTS[nid][1], SHOTS[nid][2]
        return X[col], y, CARD_W, DIMS["assets/%s.jpg" % asset][1] + CHROME
    col, y, h = DATA[nid][0], DATA[nid][1], DATA[nid][2]
    return X[col], y, CARD_W, h


def right(n):
    x, y, w, h = node_box(n); return (x + w, y + h / 2)


def left(n):
    x, y, w, h = node_box(n); return (x, y + h / 2)


def bottom(n):
    x, y, w, h = node_box(n); return (x + w / 2, y + h)


def top(n):
    x, y, w, h = node_box(n); return (x + w / 2, y)


def h_arrow(a, b, col=PAID, label=None):
    (x1, y1), (x2, y2) = right(a), left(b)
    mx = (x1 + x2) / 2
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (x1 + 6, y1, mx, y1, mx, y2, x2 - 13, y2),
              col, False, label, ((x1 + x2) / 2, min(y1, y2) - 16)))


def v_arrow(a, b, col=PAID, label=None):
    (x1, y1), (x2, y2) = bottom(a), top(b)
    my = (y1 + y2) / 2
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (x1, y1 + 6, x1, my, x2, my, x2, y2 - 13),
              col, False, label, ((x1 + x2) / 2, (y1 + y2) / 2 - 12)))


# ------- THE LIVE FUNNEL. Five real captured steps, straight line, no branches.
h_arrow("ads", "vsl", PAID, "every ad &rarr; the VSL")
h_arrow("vsl", "app", PAID, "&ldquo;60 seconds&rdquo;")
h_arrow("app", "cal", PAID, "pre-approved")
h_arrow("cal", "confirmed", PAID, "booked")
h_arrow("confirmed", "offer", PAID, "price shown on the call")

v_arrow("app", "app_detail", PAID, "the whole form is public")
v_arrow("confirmed", "objlib", PAID, "14 videos sit on this page")

# ------- WHAT IS ACTUALLY BUYING THE TRAFFIC.
v_arrow("ads", "concept", PAID, "69% of all records")
v_arrow("ads", "julywave", PROOF, "added July 2026")
v_arrow("ads", "dead2025", DEAD, "the previous offer")


def drop(nid, bx, by, col):
    """A soft dotted line from a card down to its routing-logic card."""
    x, y, w, h = node_box(nid)
    sx, sy = x + w / 2, y + h
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (sx, sy + 4, sx, (sy + by) / 2, bx + 150, (sy + by) / 2, bx + 150, by - 8),
              col, True, None, (0, 0)))


drop("concept", X[1] + 15, 2020, PAID)
drop("julywave", X[2] + 15, 2020, PROOF)
drop("dead2025", X[3] + 15, 2020, "#be123c")
drop("cal", X[4] + 15, 2020, "#be123c")
drop("objlib", X[5] + 15, 2020, "#be123c")
drop("brand", X[6] + 15, 2020, DEAD)

BANDS = [
    (125, "1 &middot; THE LIVE FUNNEL &mdash; AD &rarr; VSL &rarr; 60-SECOND TYPEFORM &rarr; CALL", PAID),
    (1375, "2 &middot; WHAT IS ACTUALLY BUYING THE TRAFFIC", PAID),
    (1995, "3 &middot; THE READ &mdash; AND WHAT WE COULD NOT SEE", "#be123c"),
]


def shot_card(nid):
    asset, col, y, lane, title, url, note = SHOTS[nid]
    a = "assets/%s.jpg" % asset
    w, h = DIMS[a]
    x, yy, cw, ch = node_box(nid)
    return (f'<a class="n {lane}" href="{url}" target="_blank" rel="noopener" '
            f'style="left:{x}px;top:{yy}px;width:{cw}px">'
            f'<div class="nh"><span class="tag">{LANE_TAG[lane]}</span>'
            f'<span class="go">open &#8599;</span></div>'
            f'<div class="nt">{title}</div><div class="nu">{url[:64]}</div>'
            f'<div class="ni" style="height:{h}px"><img src="{b64(a)}" alt=""></div>'
            f'<div class="nn">{note}</div></a>')


def data_card(nid):
    col, y, h, lane, kick, title, rows, foot = DATA[nid]
    x, yy, cw, ch = node_box(nid)
    rs = "".join(f'<div class="dr"><span>{k}</span><b>{v}</b></div>' for k, v in rows)
    return (f'<div class="n {lane}" style="left:{x}px;top:{yy}px;width:{cw}px;'
            f'height:{h}px">'
            f'<div class="nh"><span class="tag">{kick}</span></div>'
            f'<div class="nt">{title}</div><div class="drs">{rs}</div>'
            f'<div class="nn">{foot}</div></div>')


LEDE = ("Ad &rarr; 9-minute VSL &rarr; 60-second Typeform &rarr; Ben&rsquo;s Calendly. No "
        "opt-in and no email capture anywhere in the path. 360 lifetime ad records and "
        "69% of them are the same piece of copy uploaded again. The price is a one-time "
        "four figures, said out loud only after you have booked. Every screenshot below "
        "is the real page.")

W, H = 2960, 2420
paths = "".join(
    (f'<path d="{d}" stroke="{c}" stroke-width="1.6" fill="none" stroke-dasharray="5 5" '
     f'opacity=".65"/>' if dashed else
     f'<path d="{d}" stroke="{c}" stroke-width="2.5" fill="none" marker-end="url(#a{c[1:]})"/>')
    + (f'<text class="alabel" x="{lx:.0f}" y="{ly:.0f}">{lab}</text>' if lab else "")
    for d, c, dashed, lab, (lx, ly) in A)
markers = "".join(
    f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
    f'markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>'
    for c in (PAID, DEAD, PROOF))
bands = "".join(
    f'<div class="band" style="top:{y - 52}px"><span style="color:{c}">{t}</span></div>'
    for y, t, c in BANDS)
nodes = ("".join(shot_card(n) for n in SHOTS)
         + "".join(data_card(n) for n in DATA)
         + "".join(branch_card(b) for b in BRANCH))

tpl = open(os.path.join(HERE, "board_template.html")).read()
NAV = ("".join(f'<button class="w" data-go="{k}">{lab}</button>'
               for k, lab in [("funnel", "1 &middot; THE FUNNEL"),
                              ("traffic", "2 &middot; TRAFFIC"),
                              ("read", "3 &middot; THE READ"),
                              ("all", "FIT ALL")]))
VIEWS = ("{funnel:()=>frame(20,-240,2420,1450),"
         "traffic:()=>frame(20,1330,2920,620),"
         "read:()=>frame(20,1950,2920,520),"
         "all:()=>frame(0,-240,W,H+300,40)}")
KEYS = "{'1':'funnel','2':'traffic','3':'read','0':'all'}"

out = (tpl.replace("{{W}}", str(W)).replace("{{H}}", str(H))
          .replace("{{NODES}}", nodes).replace("{{BANDS}}", bands)
          .replace("{{MARKERS}}", markers).replace("{{PATHS}}", paths)
          .replace("{{KICK}}", "FUNNEL SWIPE &middot; F125 &middot; CAPTURED 6 &amp; 11 AUGUST 2026")
          .replace("{{H1}}", "Sean Ferres &mdash; Creative Strategist Breakthrough")
          .replace("{{LEDE}}", LEDE)
          .replace("{{NAV}}", NAV).replace("{{VIEWS}}", VIEWS)
          .replace("{{KEYS}}", KEYS).replace("{{HOME}}", "funnel"))
open(os.path.join(HERE, "board.html"), "w").write(out)
print(f"board.html  {len(out)/1024:.0f} KB  ({len(SHOTS)} screenshots, "
      f"{len(DATA)} data cards, {len(BRANCH)} branch cards, {len(A)} wires)")
