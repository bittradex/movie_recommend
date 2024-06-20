# Converts a 1-10 rating to a 1-5 scale and calculates the number of full, half, and empty stars.
def get_star_rating(rating):
    scaled_rating = (rating / 10) * 5
    full_stars = int(scaled_rating)
    half_star = 1 if (scaled_rating - full_stars) >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    return full_stars, half_star, empty_stars

# Generates HTML for star rating based on the given rating.
def generate_star_html(rating):
    full_stars, half_star, empty_stars = get_star_rating(rating)
    stars_html = ""
    stars_html += '<li><i class="fa fa-star" aria-hidden="true"></i></li>' * full_stars
    if half_star:
        stars_html += '<li><i class="fa fa-star-half" aria-hidden="true"></i></li>'
    stars_html += '<li><i class="fa fa-star-o" aria-hidden="true"></i></li>' * empty_stars
    return stars_html