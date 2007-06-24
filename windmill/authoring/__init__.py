#   Copyright (c) 2006-2007 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import windmill
import xmlrpclib
import new

RPC_URL = 'http://localhost:'+windmill.settings['SERVER_HTTP_PORT']+'/windmill-xmlrpc/'

class Controller(object):
    
    method_proxy = xmlrpclib.ServerProxy(RPC_URL)
    _enable_unittest = False
    enable_assertions = True
        
    def __init__(self):
        """Assign all available attributes to instance so they are easily introspected"""        
        
        class ExecuteTest(object):
            def __init__(self, method_proxy, command_name):
                self.method_proxy = method_proxy
                self.command_name = command_name
            def __call__(self, *args, **kwargs):
                getattr(self.method_proxy, self.command_name)(*args, **kwargs)
        
        class ExecuteCommand(object):
            def __init__(self, method_proxy, command_name):
                self.method_proxy = method_proxy
                self.command_name = command_name
            def __call__(self, *args, **kwargs):
                getattr(self.method_proxy, self.command_name)(*args, **kwargs)
                
                
        for attribute in self.method_proxy.getControllerMethods():
            if attribute.find('.') is -1:
                
                
    
    def enable_unittest(self, unittest_cls_inst):
        self._unittest_cls_inst = cls_inst
    
    def _exec_controller_test(self, name, **kwargs):
        result = getattr(self.method_proxy, name)(**kwargs)
        if self._enable_unittest:
            self._unittest_cls_inst.assertEqual(result, True)
        if self.enable_assertions:
            assert result is True
        return result
    
    def _exec_controller_command(self, name, **kwargs):
        result = getattr(self.method_proxy, name)(**kwargs)
        if self._enable_unittest:
            self._unittest_cls_inst.failUnless(result, 'remote call did not return proper result')
        if self.enable_assertions:
            assert result is not False
            assert result is not ''
            assert result is not None
        return result
            
                    
    
        
