# Данные для авторизации на площадках:

authorization_dev = {
    'login': 'digital',
    'pass': 'sector'}

# Энд поинты API
end_point = dict()
end_point['base_url'] = 'http://veka.ru.veka-rediz.dev.digital-sector.ru/api/'
end_point['apps'] = f'{end_point["base_url"]}{"apps?city_id=41"}'
end_point['main_page'] = f'{end_point["base_url"]}{"main-page?city_id=41"}'
end_point['select_help'] = f'{end_point["base_url"]}{"select-help?city_id=41"}'
end_point['veka_guarantee'] = f'{end_point["base_url"]}{"veka-guarantee?city_id=41"}'
end_point['cities'] = f'{end_point["base_url"]}{"cities?city_id=41"}'
end_point['detect_city'] = f'{end_point["base_url"]}{"detect-city"}'
end_point['footer'] = f'{end_point["base_url"]}{"footer?city_id=41"}'
end_point['header'] = f'{end_point["base_url"]}{"header?city_id=41"}'
#end_point['form'] = f'{end_point["base_url"]}{}'
end_point['captcha_key'] = f'{end_point["base_url"]}{"captcha-key?city_id=41"}'
#end_point['share_to_email'] = f'{end_point["base_url"]}{}'
end_point['select_help_result'] = f'{end_point["base_url"]}{"result?city_id=41&answers%5B%5D=1"}'
end_point['video_rws'] = f'{end_point["base_url"]}{"video-reviews?city_id=41&lang_id=2&limit=6"}'

#Энд поинт "Видео о окнах" зависимости от переданного Path [VideoReviews, HelpfulVideo, HelpfulVideoPartners]
end_point['video_about_windows'] = f'{end_point["base_url"]}{"video-about-windows/"}'
end_point['video_reviews'] = f'{end_point["video_about_windows"]}{"VideoReviews?city_id=41&limit=1"}'
end_point['helpful_video'] = f'{end_point["video_about_windows"]}{"HelpfulVideo?city_id=41&limit=1"}'
end_point['helpful_video_partners'] = f'{end_point["video_about_windows"]}{"HelpfulVideoPartners?city_id=41&limit=1"}'

#Энд поинт "Получение видео" зависимости от переданного Path [VideoReviews, HelpfulVideo, HelpfulVideoPartners]
end_point['videos'] = f'{end_point["base_url"]}{"videos/"}'
end_point['videos_video_reviews'] = f'{end_point["videos"]}{"VideoReviews?city_id=41&lang_id=2&limit=6"}'
end_point['videos_helpful_video'] = f'{end_point["videos"]}{"HelpfulVideo?city_id=41&limit=1"}'
end_point['videos_helpful_video_partners'] = f'{end_point["video_about_windows"]}{"HelpfulVideoPartners?city_id=41&lang_id=2&limit=6"}'
