### $ANTLR 2.7.7 (2006-11-01): "action.g" -> "ActionParser.py"$
### import antlr and other modules ..
from stringtemplate3 import antlr


### header action >>>
import stringtemplate3

### header action <<<
### preamble action>>>

### preamble action <<<

### import antlr.Token
### >>>The Known Token Types <<<
SKIP = antlr.SKIP
INVALID_TYPE = antlr.INVALID_TYPE
EOF_TYPE = antlr.EOF_TYPE
EOF = antlr.EOF
NULL_TREE_LOOKAHEAD = antlr.NULL_TREE_LOOKAHEAD
MIN_USER_TYPE = antlr.MIN_USER_TYPE
APPLY = 4
MULTI_APPLY = 5
ARGS = 6
INCLUDE = 7
CONDITIONAL = 8
VALUE = 9
TEMPLATE = 10
FUNCTION = 11
SINGLEVALUEARG = 12
LIST = 13
NOTHING = 14
SEMI = 15
LPAREN = 16
RPAREN = 17
LITERAL_elseif = 18
COMMA = 19
ID = 20
ASSIGN = 21
COLON = 22
NOT = 23
PLUS = 24
DOT = 25
LITERAL_first = 26
LITERAL_rest = 27
LITERAL_last = 28
LITERAL_length = 29
LITERAL_strip = 30
LITERAL_trunc = 31
LITERAL_super = 32
ANONYMOUS_TEMPLATE = 33
STRING = 34
INT = 35
LBRACK = 36
RBRACK = 37
DOTDOTDOT = 38
TEMPLATE_ARGS = 39
NESTED_ANONYMOUS_TEMPLATE = 40
ESC_CHAR = 41
WS = 42
WS_CHAR = 43


###/** Parse the individual attribute expressions */
class Parser(antlr.LLkParser):
    ### user action >>>
    def reportError(self, e):
        group = self.this.group
        if group == stringtemplate3.StringTemplate.defaultGroup:
            self.this.error(
                "action parse error; template context is "
                + self.this.enclosingInstanceStackString,
                e,
            )

        else:
            self.this.error(
                "action parse error in group "
                + self.this.group.name
                + " line "
                + str(self.this.groupFileLine)
                + "; template context is "
                + self.this.enclosingInstanceStackString,
                e,
            )

    ### user action <<<

    def __init__(self, *args, **kwargs):
        antlr.LLkParser.__init__(self, *args, **kwargs)
        self.tokenNames = _tokenNames
        self.buildTokenTypeASTClassMap()
        self.astFactory = antlr.ASTFactory(self.getTokenTypeToASTClassMap())
        self.astFactory.setASTNodeClass(stringtemplate3.language.StringTemplateAST)
        ### __init__ header action >>>
        if len(args) > 1 and isinstance(args[1], stringtemplate3.StringTemplate):
            self.this = args[1]
        else:
            raise ValueError("ActionParser requires a StringTemplate instance")
        ### __init__ header action <<<

    def action(self):
        opts = None

        self.returnAST = None
        currentAST = antlr.ASTPair()
        action_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [
                EOF,
                SEMI,
                LPAREN,
                COMMA,
                ID,
                COLON,
                PLUS,
                LITERAL_first,
                LITERAL_rest,
                LITERAL_last,
                LITERAL_length,
                LITERAL_strip,
                LITERAL_trunc,
                LITERAL_super,
                ANONYMOUS_TEMPLATE,
                STRING,
                INT,
                LBRACK,
            ]:
                self.templatesExpr()
                self.addASTChild(currentAST, self.returnAST)
                la1 = self.LA(1)
                if False:
                    pass
                elif la1 and la1 in [SEMI]:
                    self.match(SEMI)
                    opts = self.optionList()
                    self.addASTChild(currentAST, self.returnAST)
                elif la1 and la1 in [EOF]:
                    pass
                else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())

                action_AST = currentAST.root
            elif la1 and la1 in [CONDITIONAL]:
                tmp2_AST = None
                tmp2_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp2_AST)
                self.match(CONDITIONAL)
                self.match(LPAREN)
                self.ifCondition()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RPAREN)
                action_AST = currentAST.root
            elif la1 and la1 in [LITERAL_elseif]:
                self.match(LITERAL_elseif)
                self.match(LPAREN)
                self.ifCondition()
                self.addASTChild(currentAST, self.returnAST)
                self.match(RPAREN)
                action_AST = currentAST.root
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_0)
            else:
                raise ex

        self.returnAST = action_AST
        return opts

    def templatesExpr(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        templatesExpr_AST = None
        c = None
        c_AST = None
        try:  ## for error handling
            synPredMatched10 = False
            if (_tokenSet_1.member(self.LA(1))) and (_tokenSet_2.member(self.LA(2))):
                _m10 = self.mark()
                synPredMatched10 = True
                self.inputState.guessing += 1
                try:
                    self.parallelArrayTemplateApplication()
                except antlr.RecognitionException as pe:
                    synPredMatched10 = False
                self.rewind(_m10)
                self.inputState.guessing -= 1
            if synPredMatched10:
                self.parallelArrayTemplateApplication()
                self.addASTChild(currentAST, self.returnAST)
                templatesExpr_AST = currentAST.root
            elif (_tokenSet_3.member(self.LA(1))) and (_tokenSet_4.member(self.LA(2))):
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if self.LA(1) == COLON:
                        c = self.LT(1)
                        c_AST = self.astFactory.create(c)
                        self.makeASTRoot(currentAST, c_AST)
                        self.match(COLON)
                        if not self.inputState.guessing:
                            c_AST.setType(APPLY)
                        self.template()
                        self.addASTChild(currentAST, self.returnAST)
                        while True:
                            if self.LA(1) == COMMA:
                                self.match(COMMA)
                                self.template()
                                self.addASTChild(currentAST, self.returnAST)
                            else:
                                break

                    else:
                        break

                templatesExpr_AST = currentAST.root
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_5)
            else:
                raise ex

        self.returnAST = templatesExpr_AST

    def optionList(self):
        opts = {}

        self.returnAST = None
        currentAST = antlr.ASTPair()
        optionList_AST = None
        try:  ## for error handling
            self.option(opts)
            while True:
                if self.LA(1) == COMMA:
                    tmp9_AST = None
                    tmp9_AST = self.astFactory.create(self.LT(1))
                    self.match(COMMA)
                    self.option(opts)
                else:
                    break

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_0)
            else:
                raise ex

        self.returnAST = optionList_AST
        return opts

    def ifCondition(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        ifCondition_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [
                LPAREN,
                RPAREN,
                ID,
                PLUS,
                LITERAL_first,
                LITERAL_rest,
                LITERAL_last,
                LITERAL_length,
                LITERAL_strip,
                LITERAL_trunc,
                LITERAL_super,
                ANONYMOUS_TEMPLATE,
                STRING,
                INT,
                LBRACK,
            ]:
                self.ifAtom()
                self.addASTChild(currentAST, self.returnAST)
                ifCondition_AST = currentAST.root
            elif la1 and la1 in [NOT]:
                tmp10_AST = None
                tmp10_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp10_AST)
                self.match(NOT)
                self.ifAtom()
                self.addASTChild(currentAST, self.returnAST)
                ifCondition_AST = currentAST.root
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_6)
            else:
                raise ex

        self.returnAST = ifCondition_AST

    def option(self, opts):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        option_AST = None
        i = None
        i_AST = None
        e_AST = None
        try:  ## for error handling
            i = self.LT(1)
            i_AST = self.astFactory.create(i)
            self.addASTChild(currentAST, i_AST)
            self.match(ID)
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ASSIGN]:
                tmp11_AST = None
                tmp11_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp11_AST)
                self.match(ASSIGN)
                self.expr()
                e_AST = self.returnAST
                self.addASTChild(currentAST, self.returnAST)
                if not self.inputState.guessing:
                    v = e_AST
            elif la1 and la1 in [EOF, COMMA]:
                if not self.inputState.guessing:
                    v = stringtemplate3.language.ASTExpr.EMPTY_OPTION
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

            if not self.inputState.guessing:
                opts[i_AST.getText()] = v
            option_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_7)
            else:
                raise ex

        self.returnAST = option_AST

    def expr(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        expr_AST = None
        try:  ## for error handling
            self.primaryExpr()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if self.LA(1) == PLUS:
                    tmp12_AST = None
                    tmp12_AST = self.astFactory.create(self.LT(1))
                    self.makeASTRoot(currentAST, tmp12_AST)
                    self.match(PLUS)
                    self.primaryExpr()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break

            expr_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_8)
            else:
                raise ex

        self.returnAST = expr_AST

    def parallelArrayTemplateApplication(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        parallelArrayTemplateApplication_AST = None
        c = None
        c_AST = None
        try:  ## for error handling
            self.expr()
            self.addASTChild(currentAST, self.returnAST)
            _cnt17 = 0
            while True:
                if self.LA(1) == COMMA:
                    self.match(COMMA)
                    self.expr()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break

                _cnt17 += 1
            if _cnt17 < 1:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())
            c = self.LT(1)
            c_AST = self.astFactory.create(c)
            self.addASTChild(currentAST, c_AST)
            self.match(COLON)
            self.anonymousTemplate()
            self.addASTChild(currentAST, self.returnAST)
            if not self.inputState.guessing:
                parallelArrayTemplateApplication_AST = currentAST.root
                parallelArrayTemplateApplication_AST = antlr.make(
                    self.astFactory.create(MULTI_APPLY, "MULTI_APPLY"),
                    parallelArrayTemplateApplication_AST,
                )
                currentAST.root = parallelArrayTemplateApplication_AST
                if (parallelArrayTemplateApplication_AST != None) and (
                    parallelArrayTemplateApplication_AST.getFirstChild() != None
                ):
                    currentAST.child = (
                        parallelArrayTemplateApplication_AST.getFirstChild()
                    )
                else:
                    currentAST.child = parallelArrayTemplateApplication_AST
                currentAST.advanceChildToEnd()
            parallelArrayTemplateApplication_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_5)
            else:
                raise ex

        self.returnAST = parallelArrayTemplateApplication_AST

    def template(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        template_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LPAREN, ID, LITERAL_super]:
                self.namedTemplate()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [ANONYMOUS_TEMPLATE]:
                self.anonymousTemplate()
                self.addASTChild(currentAST, self.returnAST)
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

            if not self.inputState.guessing:
                template_AST = currentAST.root
                template_AST = antlr.make(
                    self.astFactory.create(TEMPLATE), template_AST
                )
                currentAST.root = template_AST
                if (template_AST != None) and (template_AST.getFirstChild() != None):
                    currentAST.child = template_AST.getFirstChild()
                else:
                    currentAST.child = template_AST
                currentAST.advanceChildToEnd()
            template_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_9)
            else:
                raise ex

        self.returnAST = template_AST

    def anonymousTemplate(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        anonymousTemplate_AST = None
        t = None
        t_AST = None
        try:  ## for error handling
            t = self.LT(1)
            t_AST = self.astFactory.create(t)
            self.addASTChild(currentAST, t_AST)
            self.match(ANONYMOUS_TEMPLATE)
            if not self.inputState.guessing:
                anonymous = stringtemplate3.StringTemplate()
                anonymous.group = self.this.group
                anonymous.enclosingInstance = self.this
                anonymous.template = t.getText()
                anonymous.defineFormalArgument(t.args)
                t_AST.setStringTemplate(anonymous)
            anonymousTemplate_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_9)
            else:
                raise ex

        self.returnAST = anonymousTemplate_AST

    def ifAtom(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        ifAtom_AST = None
        try:  ## for error handling
            self.expr()
            self.addASTChild(currentAST, self.returnAST)
            ifAtom_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_6)
            else:
                raise ex

        self.returnAST = ifAtom_AST

    def primaryExpr(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        primaryExpr_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [EOF, SEMI, RPAREN, COMMA, COLON, PLUS, RBRACK]:
                primaryExpr_AST = currentAST.root
            elif la1 and la1 in [
                LITERAL_first,
                LITERAL_rest,
                LITERAL_last,
                LITERAL_length,
                LITERAL_strip,
                LITERAL_trunc,
            ]:
                self.function()
                self.addASTChild(currentAST, self.returnAST)
                while True:
                    if self.LA(1) == DOT:
                        tmp14_AST = None
                        tmp14_AST = self.astFactory.create(self.LT(1))
                        self.makeASTRoot(currentAST, tmp14_AST)
                        self.match(DOT)
                        la1 = self.LA(1)
                        if False:
                            pass
                        elif la1 and la1 in [ID]:
                            tmp15_AST = None
                            tmp15_AST = self.astFactory.create(self.LT(1))
                            self.addASTChild(currentAST, tmp15_AST)
                            self.match(ID)
                        elif la1 and la1 in [LPAREN]:
                            self.valueExpr()
                            self.addASTChild(currentAST, self.returnAST)
                        else:
                            raise antlr.NoViableAltException(
                                self.LT(1), self.getFilename()
                            )

                    else:
                        break

                primaryExpr_AST = currentAST.root
            elif la1 and la1 in [LBRACK]:
                self.list_()
                self.addASTChild(currentAST, self.returnAST)
                primaryExpr_AST = currentAST.root
            else:
                synPredMatched25 = False
                if (
                    self.LA(1) == LPAREN
                    or self.LA(1) == ID
                    or self.LA(1) == LITERAL_super
                ) and (_tokenSet_10.member(self.LA(2))):
                    _m25 = self.mark()
                    synPredMatched25 = True
                    self.inputState.guessing += 1
                    try:
                        self.templateInclude()
                    except antlr.RecognitionException as pe:
                        synPredMatched25 = False
                    self.rewind(_m25)
                    self.inputState.guessing -= 1
                if synPredMatched25:
                    self.templateInclude()
                    self.addASTChild(currentAST, self.returnAST)
                    primaryExpr_AST = currentAST.root
                elif (_tokenSet_11.member(self.LA(1))) and (
                    _tokenSet_12.member(self.LA(2))
                ):
                    self.atom()
                    self.addASTChild(currentAST, self.returnAST)
                    while True:
                        if self.LA(1) == DOT:
                            tmp16_AST = None
                            tmp16_AST = self.astFactory.create(self.LT(1))
                            self.makeASTRoot(currentAST, tmp16_AST)
                            self.match(DOT)
                            la1 = self.LA(1)
                            if False:
                                pass
                            elif la1 and la1 in [ID]:
                                tmp17_AST = None
                                tmp17_AST = self.astFactory.create(self.LT(1))
                                self.addASTChild(currentAST, tmp17_AST)
                                self.match(ID)
                            elif la1 and la1 in [LPAREN]:
                                self.valueExpr()
                                self.addASTChild(currentAST, self.returnAST)
                            else:
                                raise antlr.NoViableAltException(
                                    self.LT(1), self.getFilename()
                                )

                        else:
                            break

                    primaryExpr_AST = currentAST.root
                elif (self.LA(1) == LPAREN) and (_tokenSet_13.member(self.LA(2))):
                    self.valueExpr()
                    self.addASTChild(currentAST, self.returnAST)
                    primaryExpr_AST = currentAST.root
                else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_14)
            else:
                raise ex

        self.returnAST = primaryExpr_AST

    def templateInclude(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        templateInclude_AST = None
        id = None
        id_AST = None
        qid = None
        qid_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ID]:
                id = self.LT(1)
                id_AST = self.astFactory.create(id)
                self.addASTChild(currentAST, id_AST)
                self.match(ID)
                self.argList()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [LITERAL_super]:
                self.match(LITERAL_super)
                self.match(DOT)
                qid = self.LT(1)
                qid_AST = self.astFactory.create(qid)
                self.addASTChild(currentAST, qid_AST)
                self.match(ID)
                if not self.inputState.guessing:
                    qid_AST.setText("super." + qid_AST.getText())
                self.argList()
                self.addASTChild(currentAST, self.returnAST)
            elif la1 and la1 in [LPAREN]:
                self.indirectTemplate()
                self.addASTChild(currentAST, self.returnAST)
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

            if not self.inputState.guessing:
                templateInclude_AST = currentAST.root
                templateInclude_AST = antlr.make(
                    self.astFactory.create(INCLUDE, "include"), templateInclude_AST
                )
                currentAST.root = templateInclude_AST
                if (templateInclude_AST != None) and (
                    templateInclude_AST.getFirstChild() != None
                ):
                    currentAST.child = templateInclude_AST.getFirstChild()
                else:
                    currentAST.child = templateInclude_AST
                currentAST.advanceChildToEnd()
            templateInclude_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_14)
            else:
                raise ex

        self.returnAST = templateInclude_AST

    def atom(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        atom_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ID]:
                tmp20_AST = None
                tmp20_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp20_AST)
                self.match(ID)
                atom_AST = currentAST.root
            elif la1 and la1 in [STRING]:
                tmp21_AST = None
                tmp21_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp21_AST)
                self.match(STRING)
                atom_AST = currentAST.root
            elif la1 and la1 in [INT]:
                tmp22_AST = None
                tmp22_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp22_AST)
                self.match(INT)
                atom_AST = currentAST.root
            elif la1 and la1 in [ANONYMOUS_TEMPLATE]:
                tmp23_AST = None
                tmp23_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp23_AST)
                self.match(ANONYMOUS_TEMPLATE)
                atom_AST = currentAST.root
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_12)
            else:
                raise ex

        self.returnAST = atom_AST

    def valueExpr(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        valueExpr_AST = None
        eval = None
        eval_AST = None
        try:  ## for error handling
            eval = self.LT(1)
            eval_AST = self.astFactory.create(eval)
            self.makeASTRoot(currentAST, eval_AST)
            self.match(LPAREN)
            self.templatesExpr()
            self.addASTChild(currentAST, self.returnAST)
            self.match(RPAREN)
            if not self.inputState.guessing:
                eval_AST.setType(VALUE)
                eval_AST.setText("value")
            valueExpr_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_12)
            else:
                raise ex

        self.returnAST = valueExpr_AST

    def function(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        function_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [LITERAL_first]:
                tmp25_AST = None
                tmp25_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp25_AST)
                self.match(LITERAL_first)
            elif la1 and la1 in [LITERAL_rest]:
                tmp26_AST = None
                tmp26_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp26_AST)
                self.match(LITERAL_rest)
            elif la1 and la1 in [LITERAL_last]:
                tmp27_AST = None
                tmp27_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp27_AST)
                self.match(LITERAL_last)
            elif la1 and la1 in [LITERAL_length]:
                tmp28_AST = None
                tmp28_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp28_AST)
                self.match(LITERAL_length)
            elif la1 and la1 in [LITERAL_strip]:
                tmp29_AST = None
                tmp29_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp29_AST)
                self.match(LITERAL_strip)
            elif la1 and la1 in [LITERAL_trunc]:
                tmp30_AST = None
                tmp30_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp30_AST)
                self.match(LITERAL_trunc)
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

            self.singleArg()
            self.addASTChild(currentAST, self.returnAST)
            if not self.inputState.guessing:
                function_AST = currentAST.root
                function_AST = antlr.make(
                    self.astFactory.create(FUNCTION), function_AST
                )
                currentAST.root = function_AST
                if (function_AST != None) and (function_AST.getFirstChild() != None):
                    currentAST.child = function_AST.getFirstChild()
                else:
                    currentAST.child = function_AST
                currentAST.advanceChildToEnd()
            function_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_12)
            else:
                raise ex

        self.returnAST = function_AST

    def list_(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        list__AST = None
        lb = None
        lb_AST = None
        try:  ## for error handling
            lb = self.LT(1)
            lb_AST = self.astFactory.create(lb)
            self.makeASTRoot(currentAST, lb_AST)
            self.match(LBRACK)
            if not self.inputState.guessing:
                lb_AST.setType(LIST)
                lb_AST.setText("value")
            self.listElement()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if self.LA(1) == COMMA:
                    self.match(COMMA)
                    self.listElement()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break

            self.match(RBRACK)
            list__AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_14)
            else:
                raise ex

        self.returnAST = list__AST

    def nonAlternatingTemplateExpr(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        nonAlternatingTemplateExpr_AST = None
        c = None
        c_AST = None
        try:  ## for error handling
            self.expr()
            self.addASTChild(currentAST, self.returnAST)
            while True:
                if self.LA(1) == COLON:
                    c = self.LT(1)
                    c_AST = self.astFactory.create(c)
                    self.makeASTRoot(currentAST, c_AST)
                    self.match(COLON)
                    if not self.inputState.guessing:
                        c_AST.setType(APPLY)
                    self.template()
                    self.addASTChild(currentAST, self.returnAST)
                else:
                    break

            nonAlternatingTemplateExpr_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_15)
            else:
                raise ex

        self.returnAST = nonAlternatingTemplateExpr_AST

    def singleArg(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        singleArg_AST = None
        try:  ## for error handling
            self.match(LPAREN)
            self.nonAlternatingTemplateExpr()
            self.addASTChild(currentAST, self.returnAST)
            self.match(RPAREN)
            if not self.inputState.guessing:
                singleArg_AST = currentAST.root
                singleArg_AST = antlr.make(
                    self.astFactory.create(SINGLEVALUEARG, "SINGLEVALUEARG"),
                    singleArg_AST,
                )
                currentAST.root = singleArg_AST
                if (singleArg_AST != None) and (singleArg_AST.getFirstChild() != None):
                    currentAST.child = singleArg_AST.getFirstChild()
                else:
                    currentAST.child = singleArg_AST
                currentAST.advanceChildToEnd()
            singleArg_AST = currentAST.root

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_12)
            else:
                raise ex

        self.returnAST = singleArg_AST

    def namedTemplate(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        namedTemplate_AST = None
        qid = None
        qid_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ID]:
                tmp35_AST = None
                tmp35_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp35_AST)
                self.match(ID)
                self.argList()
                self.addASTChild(currentAST, self.returnAST)
                namedTemplate_AST = currentAST.root
            elif la1 and la1 in [LITERAL_super]:
                self.match(LITERAL_super)
                self.match(DOT)
                qid = self.LT(1)
                qid_AST = self.astFactory.create(qid)
                self.addASTChild(currentAST, qid_AST)
                self.match(ID)
                if not self.inputState.guessing:
                    qid_AST.setText("super." + qid_AST.getText())
                self.argList()
                self.addASTChild(currentAST, self.returnAST)
                namedTemplate_AST = currentAST.root
            elif la1 and la1 in [LPAREN]:
                self.indirectTemplate()
                self.addASTChild(currentAST, self.returnAST)
                namedTemplate_AST = currentAST.root
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_9)
            else:
                raise ex

        self.returnAST = namedTemplate_AST

    def argList(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        argList_AST = None
        try:  ## for error handling
            if (self.LA(1) == LPAREN) and (self.LA(2) == RPAREN):
                self.match(LPAREN)
                self.match(RPAREN)
                if not self.inputState.guessing:
                    argList_AST = currentAST.root
                    argList_AST = self.astFactory.create(ARGS, "ARGS")
                    currentAST.root = argList_AST
                    if (argList_AST != None) and (argList_AST.getFirstChild() != None):
                        currentAST.child = argList_AST.getFirstChild()
                    else:
                        currentAST.child = argList_AST
                    currentAST.advanceChildToEnd()
            else:
                synPredMatched52 = False
                if (self.LA(1) == LPAREN) and (_tokenSet_16.member(self.LA(2))):
                    _m52 = self.mark()
                    synPredMatched52 = True
                    self.inputState.guessing += 1
                    try:
                        self.singleArg()
                    except antlr.RecognitionException as pe:
                        synPredMatched52 = False
                    self.rewind(_m52)
                    self.inputState.guessing -= 1
                if synPredMatched52:
                    self.singleArg()
                    self.addASTChild(currentAST, self.returnAST)
                    argList_AST = currentAST.root
                elif (self.LA(1) == LPAREN) and (
                    self.LA(2) == ID or self.LA(2) == DOTDOTDOT
                ):
                    self.match(LPAREN)
                    self.argumentAssignment()
                    self.addASTChild(currentAST, self.returnAST)
                    while True:
                        if self.LA(1) == COMMA:
                            self.match(COMMA)
                            self.argumentAssignment()
                            self.addASTChild(currentAST, self.returnAST)
                        else:
                            break

                    self.match(RPAREN)
                    if not self.inputState.guessing:
                        argList_AST = currentAST.root
                        argList_AST = antlr.make(
                            self.astFactory.create(ARGS, "ARGS"), argList_AST
                        )
                        currentAST.root = argList_AST
                        if (argList_AST != None) and (
                            argList_AST.getFirstChild() != None
                        ):
                            currentAST.child = argList_AST.getFirstChild()
                        else:
                            currentAST.child = argList_AST
                        currentAST.advanceChildToEnd()
                    argList_AST = currentAST.root
                else:
                    raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_14)
            else:
                raise ex

        self.returnAST = argList_AST

    ###/** Match (foo)() and (foo+".terse")() */
    def indirectTemplate(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        indirectTemplate_AST = None
        e_AST = None
        args_AST = None
        try:  ## for error handling
            tmp43_AST = None
            tmp43_AST = self.astFactory.create(self.LT(1))
            self.match(LPAREN)
            self.templatesExpr()
            e_AST = self.returnAST
            tmp44_AST = None
            tmp44_AST = self.astFactory.create(self.LT(1))
            self.match(RPAREN)
            self.argList()
            args_AST = self.returnAST
            if not self.inputState.guessing:
                indirectTemplate_AST = currentAST.root
                indirectTemplate_AST = antlr.make(
                    self.astFactory.create(VALUE, "value"), e_AST, args_AST
                )
                currentAST.root = indirectTemplate_AST
                if (indirectTemplate_AST != None) and (
                    indirectTemplate_AST.getFirstChild() != None
                ):
                    currentAST.child = indirectTemplate_AST.getFirstChild()
                else:
                    currentAST.child = indirectTemplate_AST
                currentAST.advanceChildToEnd()

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_14)
            else:
                raise ex

        self.returnAST = indirectTemplate_AST

    def listElement(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        listElement_AST = None
        try:  ## for error handling
            if (_tokenSet_17.member(self.LA(1))) and (_tokenSet_4.member(self.LA(2))):
                self.expr()
                self.addASTChild(currentAST, self.returnAST)
                listElement_AST = currentAST.root
            elif (self.LA(1) == COMMA or self.LA(1) == RBRACK) and (
                _tokenSet_18.member(self.LA(2))
            ):
                if not self.inputState.guessing:
                    listElement_AST = currentAST.root
                    listElement_AST = self.astFactory.create(NOTHING, "NOTHING")
                    currentAST.root = listElement_AST
                    if (listElement_AST != None) and (
                        listElement_AST.getFirstChild() != None
                    ):
                        currentAST.child = listElement_AST.getFirstChild()
                    else:
                        currentAST.child = listElement_AST
                    currentAST.advanceChildToEnd()
                listElement_AST = currentAST.root
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_19)
            else:
                raise ex

        self.returnAST = listElement_AST

    def argumentAssignment(self):
        self.returnAST = None
        currentAST = antlr.ASTPair()
        argumentAssignment_AST = None
        try:  ## for error handling
            la1 = self.LA(1)
            if False:
                pass
            elif la1 and la1 in [ID]:
                tmp45_AST = None
                tmp45_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp45_AST)
                self.match(ID)
                tmp46_AST = None
                tmp46_AST = self.astFactory.create(self.LT(1))
                self.makeASTRoot(currentAST, tmp46_AST)
                self.match(ASSIGN)
                self.nonAlternatingTemplateExpr()
                self.addASTChild(currentAST, self.returnAST)
                argumentAssignment_AST = currentAST.root
            elif la1 and la1 in [DOTDOTDOT]:
                tmp47_AST = None
                tmp47_AST = self.astFactory.create(self.LT(1))
                self.addASTChild(currentAST, tmp47_AST)
                self.match(DOTDOTDOT)
                argumentAssignment_AST = currentAST.root
            else:
                raise antlr.NoViableAltException(self.LT(1), self.getFilename())

        except antlr.RecognitionException as ex:
            if not self.inputState.guessing:
                self.reportError(ex)
                self.consume()
                self.consumeUntil(_tokenSet_15)
            else:
                raise ex

        self.returnAST = argumentAssignment_AST

    def buildTokenTypeASTClassMap(self):
        self.tokenTypeToASTClassMap = None


_tokenNames = [
    "<0>",
    "EOF",
    "<2>",
    "NULL_TREE_LOOKAHEAD",
    "APPLY",
    "MULTI_APPLY",
    "ARGS",
    "INCLUDE",
    '"if"',
    "VALUE",
    "TEMPLATE",
    "FUNCTION",
    "SINGLEVALUEARG",
    "LIST",
    "NOTHING",
    "SEMI",
    "LPAREN",
    "RPAREN",
    '"elseif"',
    "COMMA",
    "ID",
    "ASSIGN",
    "COLON",
    "NOT",
    "PLUS",
    "DOT",
    '"first"',
    '"rest"',
    '"last"',
    '"length"',
    '"strip"',
    '"trunc"',
    '"super"',
    "ANONYMOUS_TEMPLATE",
    "STRING",
    "INT",
    "LBRACK",
    "RBRACK",
    "DOTDOTDOT",
    "TEMPLATE_ARGS",
    "NESTED_ANONYMOUS_TEMPLATE",
    "ESC_CHAR",
    "WS",
    "WS_CHAR",
]


### generate bit set
def mk_tokenSet_0():
    ### var1
    data = [2, 0]
    return data


_tokenSet_0 = antlr.BitSet(mk_tokenSet_0())


### generate bit set
def mk_tokenSet_1():
    ### var1
    data = [137390260224, 0]
    return data


_tokenSet_1 = antlr.BitSet(mk_tokenSet_1())


### generate bit set
def mk_tokenSet_2():
    ### var1
    data = [274867093504, 0]
    return data


_tokenSet_2 = antlr.BitSet(mk_tokenSet_2())


### generate bit set
def mk_tokenSet_3():
    ### var1
    data = [137394094082, 0]
    return data


_tokenSet_3 = antlr.BitSet(mk_tokenSet_3())


### generate bit set
def mk_tokenSet_4():
    ### var1
    data = [274867126274, 0]
    return data


_tokenSet_4 = antlr.BitSet(mk_tokenSet_4())


### generate bit set
def mk_tokenSet_5():
    ### var1
    data = [163842, 0]
    return data


_tokenSet_5 = antlr.BitSet(mk_tokenSet_5())


### generate bit set
def mk_tokenSet_6():
    ### var1
    data = [131072, 0]
    return data


_tokenSet_6 = antlr.BitSet(mk_tokenSet_6())


### generate bit set
def mk_tokenSet_7():
    ### var1
    data = [524290, 0]
    return data


_tokenSet_7 = antlr.BitSet(mk_tokenSet_7())


### generate bit set
def mk_tokenSet_8():
    ### var1
    data = [137443835906, 0]
    return data


_tokenSet_8 = antlr.BitSet(mk_tokenSet_8())


### generate bit set
def mk_tokenSet_9():
    ### var1
    data = [4882434, 0]
    return data


_tokenSet_9 = antlr.BitSet(mk_tokenSet_9())


### generate bit set
def mk_tokenSet_10():
    ### var1
    data = [137428140032, 0]
    return data


_tokenSet_10 = antlr.BitSet(mk_tokenSet_10())


### generate bit set
def mk_tokenSet_11():
    ### var1
    data = [60130590720, 0]
    return data


_tokenSet_11 = antlr.BitSet(mk_tokenSet_11())


### generate bit set
def mk_tokenSet_12():
    ### var1
    data = [137494167554, 0]
    return data


_tokenSet_12 = antlr.BitSet(mk_tokenSet_12())


### generate bit set
def mk_tokenSet_13():
    ### var1
    data = [137394585600, 0]
    return data


_tokenSet_13 = antlr.BitSet(mk_tokenSet_13())


### generate bit set
def mk_tokenSet_14():
    ### var1
    data = [137460613122, 0]
    return data


_tokenSet_14 = antlr.BitSet(mk_tokenSet_14())


### generate bit set
def mk_tokenSet_15():
    ### var1
    data = [655360, 0]
    return data


_tokenSet_15 = antlr.BitSet(mk_tokenSet_15())


### generate bit set
def mk_tokenSet_16():
    ### var1
    data = [137394061312, 0]
    return data


_tokenSet_16 = antlr.BitSet(mk_tokenSet_16())


### generate bit set
def mk_tokenSet_17():
    ### var1
    data = [274829213696, 0]
    return data


_tokenSet_17 = antlr.BitSet(mk_tokenSet_17())


### generate bit set
def mk_tokenSet_18():
    ### var1
    data = [274833571842, 0]
    return data


_tokenSet_18 = antlr.BitSet(mk_tokenSet_18())


### generate bit set
def mk_tokenSet_19():
    ### var1
    data = [137439477760, 0]
    return data


_tokenSet_19 = antlr.BitSet(mk_tokenSet_19())
