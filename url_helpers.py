
class URLHelpers:
    @staticmethod
    def url_for(static_folder, filename, **kwargs):
        static_path = f'/static/{static_folder}/{filename}'

        if kwargs:
            query_string = '&'.join(f'{key}={value}' for key, value in kwargs.items())
            static_path = f'{static_path}?{query_string}'

        return static_path
# Generate a URL for a static file
url = URLHelpers.url_for('css', 'styles.css', version=1, lang='en')

# Print the generated URL
print(url)
