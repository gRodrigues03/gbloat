PACKAGES = [
    'com.samsung.android.forest',
    'com.google.android.apps.wellbeing',
    'com.samsung.android.themestore',
    'com.samsung.android.app.tips',

    'com.samsung.android.bixby.agent',
    'com.samsung.android.bixby.wakeup',
    'com.samsung.android.bixby.service',
    'com.samsung.android.bixbyvision.framework',
    'com.samsung.android.visionintelligence',
    'com.samsung.android.app.spage',
    'com.samsung.android.aremoji',
    'com.samsung.android.aremojieditor',
    'com.sec.android.mimage.avatarstickers',
    'com.samsung.android.livestickers',
    'com.samsung.android.stickercenter',
    'com.samsung.android.app.parentalcare',

    'com.samsung.android.hmt.vrsvc',
    'com.samsung.android.hmt.vrshell',
    'com.google.vr.vrcore',
    'com.google.android.apps.tachyon',
    'com.google.android.videos',
    'com.google.android.apps.carrier.carrierwifi',

    'com.sec.android.diagmonagent',
    'com.samsung.android.rubin.app',

    'com.samsung.android.arzone',
    'com.samsung.android.ardrawing',
    'com.samsung.android.kidsinstaller',
    'com.sec.android.app.kidshome',
    'com.google.android.aicore',
    'com.google.ar.core',
    'com.samsung.SMT.lang_hi_in_f00',
    'com.samsung.SMT.lang_ar_ae_m00',
    'com.samsung.android.smartsuggestions',
    'com.samsung.android.vision.model',
    'com.google.android.as',
    'com.samsung.android.intelligenceservice',
    "com.samsung.android.scs",
    "package:com.samsung.SMT.lang_fr_fr_f00",
    "package:com.samsung.SMT.lang_th_th_f00",
    "package:com.samsung.SMT.lang_id_id_f00",
    "package:com.samsung.SMT.lang_pl_pl_f00",
    "package:com.samsung.SMT.lang_it_it_f00",
    "package:com.samsung.SMT.lang_de_de_f00",
    "package:com.samsung.SMT.lang_vi_vn_f00",
    "package:com.samsung.android.offline.languagemodel",
]

with open('commands.bat', 'w', encoding='utf-8') as f:
    for package in PACKAGES:
        f.write(f'adb shell pm uninstall-system-updates {package}\n')
        f.write(f'adb shell pm uninstall --user 0 {package}\n')
        f.write(f'adb shell pm disable-user --user 0 {package}\n')
