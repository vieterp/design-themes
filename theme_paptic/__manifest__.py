{
    'name': 'Paptic Theme',
    'description': 'Clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Consultancy, Design, Tech, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['website'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/paptic_poster.jpg',
        'static/description/paptic_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-paptic.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_paptic/static/src/js/tour.js',
        ],
    }
}
