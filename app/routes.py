from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/fav')
def favorite():
    fav_5 = [
        {'title' : 'Mine',
         'artist' : 'Kelly Clarkson',
         'spotify_link' : 'https://open.spotify.com/embed/track/20XB21FHWhdyWTs5z7p9Vl?utm_source=generator',
         'description' : '"Mine" is a song by American pop recording artist Kelly Clarkson, from her tenth studio album, Chemistry (2023). Accompanied with "Me", it was released on April 14, 2023, by Atlantic Records as the lead double A-side single. It was written by Clarkson, Eric Serna, Jesse Shatkin, and produced by Serna and Shatkin.'
         },
        {'title' : 'Summer Reinassaince',
         'artist' : 'Beyoncé',
         'spotify_link' : 'https://open.spotify.com/embed/track/3HyR1j49TY5ACP2lseF1jx?utm_source=generator',
         'description' : '“SUMMER RENAISSANCE” is the closing track on Beyoncé’s seventh studio album, RENAISSANCE, sampling “I Feel Love” by Donna Summer.\n\nThe track title itself is a tribute to the Queen of Disco using her stage name “SUMMER” followed by “RENAISSANCE,” which means “re-birth” in French.\n\nBeyoncé states in the last track of the album, that the message being portrayed is a celebration, rebirth & innovation of past sounds (such as disco, house, vogue & ballroom) that were founded by artists as – for example – Donna Summer.'
         },
        {'title' : 'Skip this Part',
         'artist' : 'Kelly Clarkson',
         'spotify_link' : 'https://open.spotify.com/embed/track/5OniCi8mdZXcJ9nTvIctID?utm_source=generator',
         'description' : 'Can i skip this part? this is the opening track on my new album #chemistry out June 23rd.'
         },
        {'title' : 'The One That Got Away',
         'artist' : 'Katy Perry',
         'spotify_link' : 'https://open.spotify.com/embed/track/5jx8tCxiO0uIbo2uNia23K?utm_source=generator',
         'description' : 'The One That Got Away" is a song by American singer-songwriter Katy Perry from her third studio album, Teenage Dream (2010). The song was produced by Dr. Luke and Max Martin, both of whom also co-wrote the song with Perry. The song is a mid-tempo pop ballad about a lost love. It features a reference to the rock band Radiohead, and compares the strength of the relationship to that of Johnny Cash and June Carter Cash. The song was released on September 30, 2011, by Capitol Records as the album\'s sixth single.\n\n"The One That Got Away" peaked at number three on the Billboard Hot 100, with Teenage Dream becoming the seventh album in the 53-year history of the Hot 100 to generate at least six top 10s. The single reached the top of the Billboard Hot Dance Club Songs, Adult Top 40, and Mainstream Top 40 charts.\n\nThe accompanying music video for the song was directed by Floria Sigismondi and premiered in November 2011, featuring actor Diego Luna. An official remix featuring rapper B.o.B was released to digital retailers on December 20, 2011.[1] An official acoustic rendition was released to digital retailers on January 16, 2012, this version was included in Teenage Dream: The Complete Confection edition.[2] The song has been covered by several artists, including Kelly Clarkson,[3] Olivia Rodrigo and Conan Gray, Richard Marx, Jordan Pruitt, Selena Gomez & the Scene, and Tate McRae.'
         },
        {'title' : 'Come Clean',
         'artist' : 'Hillary Duff',
         'spotify_link' : 'https://open.spotify.com/embed/track/2TZ1apxMDlubCGMsOxcTbT?utm_source=generator',
         'description' : '"Come Clean" is a song by American singer Hilary Duff for her second studio album, Metamorphosis (2003). It was written by Kara DioGuardi and John Shanks, while production was handled by Shanks. The song contains influences of electronica and techno, with the lyrics chronicling the protagonist wanting to "come clean" with her love interest, from a strained relationship. "Come Clean" was received by critics with mixed reviews. The song was released on January 12, 2004, as the album\'s second single.\n\nIn the United States, the song peaked at number 35, becoming Duff\'s first top-40 single on the Billboard Hot 100. It would later go on to become her best-selling single in the United States.[1] However, the song failed to match the success of its predecessor "So Yesterday" in many other countries. It reached number 17 in Australia and number 18 in the United Kingdom while charting within the top 20 in Canada, Ireland, the Netherlands, and New Zealand. A remix of the song by Chris Cox was included in Duff\'s 2005 compilation album, Most Wanted, this version was also included on her Dignity Walmart edition Remix EP as the Dance Mix in 2007, and in 2008, another remix of the song by Chico Bennett & Richard "Humpty" Vission was included in Best of Hilary Duff while the original version is included on the Japanese edition.\n\nThe song was accompanied by a music video, directed Dave Meyers, which showed Duff inside a house on a rainy day, waiting for her love interest. The video was nominated in the category of Best Pop Video at the 2004 MTV Video Music Awards. The song was used in the theatrical trailer for the 2004 film A Cinderella Story, which stars Duff. It was used as the theme song for the MTV reality television shows Laguna Beach: The Real Orange County and Newport Harbor: The Real Orange County, and it is included on the soundtrack album for Laguna Beach.'
         },
        
    ]
    return render_template('favorite.html', fav_5 = fav_5, len = len(fav_5))