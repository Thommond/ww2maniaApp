import postgres
import pytest


# def test_get_close_db(app):
#     with app.app_context():
#         db = get_db()
#         assert db is get_db()
#
#     with pytest.raises(postgres.ProgrammingError) as e:
#         db.execute('SELECT 1')
#
#     assert 'closed' in str(e.value)
#
#
# def test_init_db_command(runner, monkeypatch):
#     class Record(object):
#         called = False
#
#     def fake_init_db():
#         Record.called = True
#
#     monkeypatch.setattr('ww2mania.db.init_db', fake_init_db)
#     result = runner.invoke(arg=['init-db'])
#     assert 'Initialized' in result.output
#     assert Recorder.called
