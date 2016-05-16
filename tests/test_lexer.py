import demolex

class TestLexer:
  def test_lexer(self):
    demolex.lexer.input('1')
    tok = demolex.lexer.token()
    print(tok)
