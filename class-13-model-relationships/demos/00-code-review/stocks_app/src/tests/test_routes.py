class TestClass:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_home_route_get(self, app):
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert b'<h1>Welcome to the site</h1>' in rv.data

    def test_home_route_post(self, app):
        rv = app.test_client().post('/')
        assert rv.status_code == 405

    def test_home_route_delete(self, app):
        rv = app.test_client().delete('/')
        assert rv.status_code == 405

    def test_search_route_get(self, app):
        rv = app.test_client().get('/search')
        assert rv.status_code == 200
        assert b'<h2>Search for stocks</h2>' in rv.data

    def test_search_post_pre_redirect(self, app, db):
        rv = app.test_client().post('/search', data = {'symbol' : 'amzn'})
        assert rv.status_code == 302

    def test_search_post_with_repeat(self, app, db):
        rv = app.test_client().post('/search', data = {'symbol' : 'amzn'})
        assert rv.status_code == 302

    def test_search_post(self, app, db):
        rv = app.test_client().post('/search', data = {'symbol' : 'amzn'}, follow_redirects = True)
        assert rv.status_code == 200
        assert b'<input type="submit" value="Add to Portfolio">' in rv.data

    def test_bunk_symbol(self, app):
        rv = app.test_client().post('/search', data = {'symbol' : 'superunknown'}, follow_redirects=True)
        assert rv.status_code == 200
        assert b'<div class="flash">The company you searched for does not exist.</div>' in rv.data


    def test_url_for(self, app):
        rv = app.test_client().get('/')
        assert b'<a href="/search"' in rv.data
        assert b'<a href="/portfolio"' in rv.data
        assert b'<link rel="stylesheet" href="/css/normalize.css">' in rv.data

    def test_portfolio_route_get(self, app, db):
        pass
        # DANGER: running below code introduces a really nasty crash
        # see if you can figure out why

        # rv = app.test_client().get('/portfolio')
        # assert rv.status_code == 200
        # assert b'<h2>Welcome to the Portfolio</h2>' in rv.data
