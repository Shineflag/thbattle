# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
# -- own --
from client.ui.resloader import get_atlas, inventory

# -- code --
import gamepack.thb.ui.ui_meta  # noqa

get_atlas('portrait', (1024, 2048))

inventory.update({
    'thb-bgm_game':                        ['bgm'],

    'thb-modelogo-3v3':                    ['img'],
    'thb-modelogo-8id':                    ['img'],
    'thb-modelogo-5id':                    ['img'],
    'thb-modelogo-kof':                    ['img'],
    'thb-modelogo-raid':                   ['img'],
    'thb-modelogo-faith':                  ['img'],
    'thb-modelogo-cp3':                    ['img'],
    'thb-modelogo-2v2':                    ['img'],

    'thb-win':                             ['img'],
    'thb-lose':                            ['img'],
    'thb-hurt':                            ['anim', [50, 50, 50, 50, 200, 30, 30, 30, 30, 2000]],

    'thb-card-shinesoft':                  ['img', 'card'],
    'thb-card-hidden':                     ['img', 'card'],
    'thb-card-question':                   ['img', 'card'],
    'thb-card-showncardtag':               ['img', 'card'],

    'thb-card-attack':                     ['img', 'card'],
    'thb-card-graze':                      ['img', 'card'],
    'thb-card-heal':                       ['img', 'card'],
    'thb-card-demolition':                 ['img', 'card'],
    'thb-card-reject':                     ['img', 'card'],
    'thb-card-sealarray':                  ['img', 'card'],
    'thb-card-nazrinrod':                  ['img', 'card'],
    'thb-card-opticalcloak':               ['img', 'card'],
    'thb-card-greenufo':                   ['img', 'card'],
    'thb-card-redufo':                     ['img', 'card'],
    'thb-card-sinsack':                    ['img', 'card'],
    'thb-card-yukaridimension':            ['img', 'card'],
    'thb-card-duel':                       ['img', 'card'],
    'thb-card-sinsackcarnival':            ['img', 'card'],
    'thb-card-mapcannon':                  ['img', 'card'],
    'thb-card-hakurouken':                 ['img', 'card'],
    'thb-card-reactor':                    ['img', 'card'],
    'thb-card-umbrella':                   ['img', 'card'],
    'thb-card-roukanken':                  ['img', 'card'],
    'thb-card-gungnir':                    ['img', 'card'],
    'thb-card-laevatein':                  ['img', 'card'],
    'thb-card-repentancestick':            ['img', 'card'],
    'thb-card-wine':                       ['img', 'card'],
    'thb-card-feast':                      ['img', 'card'],
    'thb-card-harvest':                    ['img', 'card'],
    'thb-card-maidencostume':              ['img', 'card'],
    'thb-card-exinwan':                    ['img', 'card'],
    'thb-card-ibukigourd':                 ['img', 'card'],
    'thb-card-houraijewel':                ['img', 'card'],
    'thb-card-saigyoubranch':              ['img', 'card'],
    'thb-card-ayaroundfan':                ['img', 'card'],
    'thb-card-scarletrhapsodysword':       ['img', 'card'],
    'thb-card-deathsickle':                ['img', 'card'],
    'thb-card-keystone':                   ['img', 'card'],
    'thb-card-witchbroom':                 ['img', 'card'],
    'thb-card-yinyangorb':                 ['img', 'card'],
    'thb-card-suwakohat':                  ['img', 'card'],
    'thb-card-phantom':                    ['img', 'card'],
    'thb-card-icewing':                    ['img', 'card'],
    'thb-card-grimoire':                   ['img', 'card'],
    'thb-card-dollcontrol':                ['img', 'card'],
    'thb-card-donationbox':                ['img', 'card'],
    'thb-card-frozenfrog':                 ['img', 'card'],
    'thb-card-nenshaphone':                ['img', 'card'],
    'thb-card-momijishield':               ['img', 'card'],

    'thb-card-small-opticalcloak':         ['img', 'card'],
    'thb-card-small-greenufo':             ['img', 'card'],
    'thb-card-small-redufo':               ['img', 'card'],
    'thb-card-small-hakurouken':           ['img', 'card'],
    'thb-card-small-reactor':              ['img', 'card'],
    'thb-card-small-umbrella':             ['img', 'card'],
    'thb-card-small-roukanken':            ['img', 'card'],
    'thb-card-small-gungnir':              ['img', 'card'],
    'thb-card-small-laevatein':            ['img', 'card'],
    'thb-card-small-repentancestick':      ['img', 'card'],
    'thb-card-small-maidencostume':        ['img', 'card'],
    'thb-card-small-ibukigourd':           ['img', 'card'],
    'thb-card-small-houraijewel':          ['img', 'card'],
    'thb-card-small-saigyoubranch':        ['img', 'card'],
    'thb-card-small-ayaroundfan':          ['img', 'card'],
    'thb-card-small-scarletrhapsodysword': ['img', 'card'],
    'thb-card-small-deathsickle':          ['img', 'card'],
    'thb-card-small-keystone':             ['img', 'card'],
    'thb-card-small-witchbroom':           ['img', 'card'],
    'thb-card-small-yinyangorb':           ['img', 'card'],
    'thb-card-small-suwakohat':            ['img', 'card'],
    'thb-card-small-phantom':              ['img', 'card'],
    'thb-card-small-icewing':              ['img', 'card'],
    'thb-card-small-grimoire':             ['img', 'card'],
    'thb-card-small-nenshaphone':          ['img', 'card'],
    'thb-card-small-momijishield':         ['img', 'card'],

    'thb-card-small-frame':                ['img', 'card'],
    'thb-card-small-selected':             ['img', 'card'],

    'thb-cardnum':                         ['img_grid', 2, 13, 'card'],
    'thb-suit':                            ['img_grid', 1, 4,  'card'],
    'thb-smallsuit':                       ['img_grid', 1, 4,  'card'],
    'thb-smallnum':                        ['img_grid', 2, 14, 'card'],

    'thb-tag-sealarray':                   ['anim', [83] * 36,  True],
    'thb-tag-wine':                        ['anim', [150] * 3,  True],
    'thb-tag-lunadial':                    ['anim', [200] * 10, True],
    'thb-tag-riverside':                   ['img'],
    'thb-tag-action':                      ['img'],
    'thb-tag-attacked':                    ['img'],
    'thb-tag-flandrecs':                   ['img'],
    'thb-tag-flandre_exterminate':         ['img'],
    'thb-tag-frozenfrog':                  ['img'],
    'thb-tag-gameintro':                   ['img'],
    'thb-tag-sinsack':                     ['img'],
    'thb-tag-ran_ei':                      ['img'],
    'thb-tag-aya_range_max':               ['img'],
    'thb-tag-aya_range_max':               ['img'],
    'thb-tag-faiths':                      ['img_grid', 1, 7],
    'thb-tag-reisen_discarder':            ['img'],

    'thb-portrait-parsee':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-youmu':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-koakuma':                ['img_with_grayed', 'portrait'],
    'thb-portrait-marisa':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-daiyousei':              ['img_with_grayed', 'portrait'],
    'thb-portrait-flandre':                ['img_with_grayed', 'portrait'],
    'thb-portrait-nazrin':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-alice':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-yugi':                   ['img_with_grayed', 'portrait'],
    'thb-portrait-tewi':                   ['img_with_grayed', 'portrait'],
    'thb-portrait-patchouli':              ['img_with_grayed', 'portrait'],
    'thb-portrait-reimu':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-eirin':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-kogasa':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-shikieiki':              ['img_with_grayed', 'portrait'],
    'thb-portrait-tenshi':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-rumia':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-yuuka':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-rinnosuke':              ['img_with_grayed', 'portrait'],
    'thb-portrait-ran':                    ['img_with_grayed', 'portrait'],
    'thb-portrait-remilia':                ['img_with_grayed', 'portrait'],
    'thb-portrait-minoriko':               ['img_with_grayed', 'portrait'],
    'thb-portrait-meirin':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-suika':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-chen':                   ['img_with_grayed', 'portrait'],
    'thb-portrait-yukari':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-cirno':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-sakuya':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-sanae':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-akari':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-seiga':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-kaguya':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-momiji':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-komachi':                ['img_with_grayed', 'portrait'],
    'thb-portrait-mokou':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-kokoro':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-mamizou':                ['img_with_grayed', 'portrait'],
    'thb-portrait-seija':                  ['img_with_grayed', 'portrait'],
    'thb-portrait-kanako':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-medicine':               ['img_with_grayed', 'portrait'],
    'thb-portrait-aya':                    ['img_with_grayed', 'portrait'],
    'thb-portrait-sp_yukari':              ['img_with_grayed', 'portrait'],
    'thb-portrait-sp_flandre':             ['img_with_grayed', 'portrait'],
    'thb-portrait-reisen':                 ['img_with_grayed', 'portrait'],
    'thb-portrait-remilia_ex':             ['img_with_grayed', 'portrait'],
    'thb-portrait-remilia_ex2':            ['img_with_grayed', 'portrait'],

    'thb-figure-daiyousei':                ['lazytexture'],
    'thb-figure-eirin':                    ['lazytexture'],
    'thb-figure-koakuma':                  ['lazytexture'],
    'thb-figure-yukari':                   ['lazytexture'],
    'thb-figure-komachi':                  ['lazytexture'],
    'thb-figure-kokoro':                   ['lazytexture'],
    'thb-figure-cirno':                    ['lazytexture'],
    'thb-figure-patchouli':                ['lazytexture'],
    'thb-figure-yugi':                     ['lazytexture'],
    'thb-figure-aya':                      ['lazytexture'],
    'thb-figure-sp_yukari':                ['lazytexture'],
    'thb-figure-sp_flandre':               ['lazytexture'],
    'thb-figure-sakuya':                   ['lazytexture'],
    'thb-figure-alice':                    ['lazytexture'],
    'thb-figure-kogasa':                   ['lazytexture'],
    'thb-figure-remilia':                  ['lazytexture'],
    'thb-figure-reisen':                   ['lazytexture'],

    'thb-figure-komachi_alter':            ['encrypted_texture'],
    'thb-figure-patchouli_alter':          ['encrypted_texture'],

    'thb-hp':                              ['img_with_grayed', 'portrait'],
    'thb-hp_bg':                           ['img_with_grayed', 'portrait'],

    'thb-num':                             ['img_grid', 1, 10, 'portrait'],

    'thb-remilia_ex_wallpaper':            ['texture'],

    'thb-bgm_remilia_ex':                  ['bgm'],

    'thb-sound-hit':                       ['sound'],

    'thb-cv-alice_legion':                 ['sound'],
    'thb-cv-alice_miss':                   ['sound'],
    'thb-cv-aya_miss':                     ['sound'],
    'thb-cv-aya_ultimatespeed':            ['sound'],
    'thb-cv-card_attack1':                 ['sound'],
    'thb-cv-card_attack2':                 ['sound'],
    'thb-cv-card_attack3':                 ['sound'],
    'thb-cv-card_attack4':                 ['sound'],
    'thb-cv-card_deathsickle':             ['sound'],
    'thb-cv-card_demolition':              ['sound'],
    'thb-cv-card_dimension':               ['sound'],
    'thb-cv-card_dollcontrol':             ['sound'],
    'thb-cv-card_donationbox':             ['sound'],
    'thb-cv-card_duel':                    ['sound'],
    'thb-cv-card_exinwan':                 ['sound'],
    'thb-cv-card_feast1':                  ['sound'],
    'thb-cv-card_feast2':                  ['sound'],
    'thb-cv-card_feast3':                  ['sound'],
    'thb-cv-card_frozenfrog':              ['sound'],
    'thb-cv-card_graze1':                  ['sound'],
    'thb-cv-card_graze2':                  ['sound'],
    'thb-cv-card_graze3':                  ['sound'],
    'thb-cv-card_graze4':                  ['sound'],
    'thb-cv-card_grimoire':                ['sound'],
    'thb-cv-card_hakurouken':              ['sound'],
    'thb-cv-card_harvest':                 ['sound'],
    'thb-cv-card_heal':                    ['sound'],
    'thb-cv-card_icewing':                 ['sound'],
    'thb-cv-card_keystone':                ['sound'],
    'thb-cv-card_laevatein':               ['sound'],
    'thb-cv-card_mapcannon':               ['sound'],
    'thb-cv-card_momijishield':            ['sound'],
    'thb-cv-card_nazrinrod':               ['sound'],
    'thb-cv-card_nenshaphone':             ['sound'],
    'thb-cv-card_opticalcloak':            ['sound'],
    'thb-cv-card_phantom':                 ['sound'],
    'thb-cv-card_reject':                  ['sound'],
    'thb-cv-card_repentancestick':         ['sound'],
    'thb-cv-card_roukanken':               ['sound'],
    'thb-cv-card_roundfan1':               ['sound'],
    'thb-cv-card_roundfan2':               ['sound'],
    'thb-cv-card_saigyoubranch':           ['sound'],
    'thb-cv-card_sealarray':               ['sound'],
    'thb-cv-card_sinsack':                 ['sound'],
    'thb-cv-card_sinsack_effect':          ['sound'],
    'thb-cv-card_sinsackcarnival':         ['sound'],
    'thb-cv-card_srs':                     ['sound'],
    'thb-cv-card_suwakohat':               ['sound'],
    'thb-cv-card_umbrella':                ['sound'],
    'thb-cv-card_wine':                    ['sound'],
    'thb-cv-chen_miss':                    ['sound'],
    'thb-cv-chen_shikigami':               ['sound'],
    'thb-cv-chen_skanda':                  ['sound'],
    'thb-cv-cirno_miss':                   ['sound'],
    'thb-cv-cirno_perfectfreeze':          ['sound'],
    'thb-cv-daiyousei_miss':               ['sound'],
    'thb-cv-daiyousei_moe':                ['sound'],
    'thb-cv-daiyousei_support':            ['sound'],
    'thb-cv-eirin_firstaid':               ['sound'],
    'thb-cv-eirin_medic':                  ['sound'],
    'thb-cv-eirin_miss':                   ['sound'],
    'thb-cv-flandre_cs':                   ['sound'],
    'thb-cv-flandre_miss':                 ['sound'],
    'thb-cv-kaguya_dilemma1':              ['sound'],
    'thb-cv-kaguya_dilemma2':              ['sound'],
    'thb-cv-kaguya_inight':                ['sound'],
    'thb-cv-kaguya_miss':                  ['sound'],
    'thb-cv-kanako_divinity':              ['sound'],
    'thb-cv-kanako_faith':                 ['sound'],
    'thb-cv-kanako_miss':                  ['sound'],
    'thb-cv-kanako_virtue':                ['sound'],
    'thb-cv-koakuma_find':                 ['sound'],
    'thb-cv-koakuma_miss':                 ['sound'],
    'thb-cv-kogasa_jolly':                 ['sound'],
    'thb-cv-kogasa_miss':                  ['sound'],
    'thb-cv-kogasa_surprise':              ['sound'],
    'thb-cv-kokoro_darknoh':               ['sound'],
    'thb-cv-kokoro_hopemask':              ['sound'],
    'thb-cv-kokoro_miss':                  ['sound'],
    'thb-cv-komachi_awake':                ['sound'],
    'thb-cv-komachi_ferryfee':             ['sound'],
    'thb-cv-komachi_miss':                 ['sound'],
    'thb-cv-komachi_riverside':            ['sound'],
    'thb-cv-mamizou_miss':                 ['sound'],
    'thb-cv-mamizou_morph':                ['sound'],
    'thb-cv-marisa_borrow':                ['sound'],
    'thb-cv-marisa_miss':                  ['sound'],
    'thb-cv-medicine_ciguatera':           ['sound'],
    'thb-cv-medicine_melancholy':          ['sound'],
    'thb-cv-medicine_miss':                ['sound'],
    'thb-cv-meirin_loongpunch':            ['sound'],
    'thb-cv-meirin_miss1':                 ['sound'],
    'thb-cv-meirin_miss2':                 ['sound'],
    'thb-cv-meirin_rb':                    ['sound'],
    'thb-cv-meirin_taichi':                ['sound'],
    'thb-cv-minoriko_akitribute':          ['sound'],
    'thb-cv-minoriko_autumnfeast':         ['sound'],
    'thb-cv-minoriko_foison':              ['sound'],
    'thb-cv-minoriko_miss':                ['sound'],
    'thb-cv-mokou_ashes':                  ['sound'],
    'thb-cv-mokou_miss':                   ['sound'],
    'thb-cv-mokou_reborn':                 ['sound'],
    'thb-cv-momiji_miss':                  ['sound'],
    'thb-cv-momiji_sentry1':               ['sound'],
    'thb-cv-momiji_sentry2':               ['sound'],
    'thb-cv-nazrin_agile':                 ['sound'],
    'thb-cv-nazrin_miss':                  ['sound'],
    'thb-cv-nazrin_treasurehunt':          ['sound'],
    'thb-cv-parsee_envy':                  ['sound'],
    'thb-cv-parsee_miss':                  ['sound'],
    'thb-cv-patchouli_knowledge':          ['sound'],
    'thb-cv-patchouli_library1':           ['sound'],
    'thb-cv-patchouli_library2':           ['sound'],
    'thb-cv-patchouli_miss':               ['sound'],
    'thb-cv-ran_ei':                       ['sound'],
    'thb-cv-ran_miss':                     ['sound'],
    'thb-cv-ran_prophet':                  ['sound'],
    'thb-cv-reimu_miss':                   ['sound'],
    'thb-cv-reimu_sa':                     ['sound'],
    'thb-cv-reisen_lunatic':               ['sound'],
    'thb-cv-reisen_mahjongdrug':           ['sound'],
    'thb-cv-remilia_miss':                 ['sound'],
    'thb-cv-remilia_stg':                  ['sound'],
    'thb-cv-remilia_vampirekiss':          ['sound'],
    'thb-cv-rinnosuke_miss':               ['sound'],
    'thb-cv-rinnosuke_nitoru':             ['sound'],
    'thb-cv-rinnosuke_psycopath':          ['sound'],
    'thb-cv-rumia_cheat':                  ['sound'],
    'thb-cv-rumia_darkness':               ['sound'],
    'thb-cv-rumia_miss':                   ['sound'],
    'thb-cv-sakuya_dagger1':               ['sound'],
    'thb-cv-sakuya_dagger2':               ['sound'],
    'thb-cv-sakuya_lunadial':              ['sound'],
    'thb-cv-sakuya_miss':                  ['sound'],
    'thb-cv-sanae_faith':                  ['sound'],
    'thb-cv-sanae_goddescendant1':         ['sound'],
    'thb-cv-sanae_goddescendant2':         ['sound'],
    'thb-cv-sanae_miracle':                ['sound'],
    'thb-cv-sanae_miss':                   ['sound'],
    'thb-cv-seiga_heterodoxy':             ['sound'],
    'thb-cv-seiga_miss':                   ['sound'],
    'thb-cv-seija_incite1':                ['sound'],
    'thb-cv-seija_incite2':                ['sound'],
    'thb-cv-seija_miss':                   ['sound'],
    'thb-cv-seija_reversal':               ['sound'],
    'thb-cv-shikieiki_majesty':            ['sound'],
    'thb-cv-shikieiki_miss':               ['sound'],
    'thb-cv-shikieiki_trial1':             ['sound'],
    'thb-cv-shikieiki_trial2':             ['sound'],
    'thb-cv-spflandre_destructionimpulse': ['sound'],
    'thb-cv-spflandre_fourofakind':        ['sound'],
    'thb-cv-spflandre_miss':               ['sound'],
    'thb-cv-spyukari_miss':                ['sound'],
    'thb-cv-spyukari_spiritaway1':         ['sound'],
    'thb-cv-spyukari_spiritaway2':         ['sound'],
    'thb-cv-suika_drunkard':               ['sound'],
    'thb-cv-suika_miss':                   ['sound'],
    'thb-cv-suika_winegod':                ['sound'],
    'thb-cv-tenshi_masochist':             ['sound'],
    'thb-cv-tenshi_miss':                  ['sound'],
    'thb-cv-tenshi_sp':                    ['sound'],
    'thb-cv-tewi_lucky':                   ['sound'],
    'thb-cv-tewi_miss':                    ['sound'],
    'thb-cv-youmu_miss':                   ['sound'],
    'thb-cv-youmu_mjchz':                  ['sound'],
    'thb-cv-youmu_nitoryuu':               ['sound'],
    'thb-cv-yugi_fp1':                     ['sound'],
    'thb-cv-yugi_fp2':                     ['sound'],
    'thb-cv-yugi_miss':                    ['sound'],
    'thb-cv-yuuka_flowerqueen':            ['sound'],
    'thb-cv-yuuka_miss':                   ['sound'],
    'thb-cv-yuuka_rs':                     ['sound'],
    'thb-cv-yuuka_sadist':                 ['sound'],
})
