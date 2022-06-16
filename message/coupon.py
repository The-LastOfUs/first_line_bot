from dataclasses import dataclass
import re
from typing import Callable, List, Match

@dataclass
class Command:
    regular: str
    handle: Callable[[Match[str]], str]

@dataclass
class CouponBotMessageHandle:
    commands: List[Command]

    def handle(self, message: str):
        for cmd in self.commands:
            print(cmd.regular)
            print(re.match(cmd.regular, message))
            if (re.match(cmd.regular, message)):
                return cmd.handle(re.compile(cmd.regular).search(message))

    
def __handle_use(match_res: Match[str]) -> str:
    coupon_id = match_res.group(1)
    return '已使用優惠券: ' + coupon_id

def __handle_add_to_all(match_res: Match[str]) -> str:
    coupon_id = match_res.group(1)
    return '已發放優惠券 {id} to all'.format(id=coupon_id)

def __handle_add_to_user_id(match_res: Match[str]) -> str:
    return '已發放優惠券 {id} to user: {user}'.format(id=match_res.group(1), user=match_res.group(2))

def __handle_create_coupon(match_res: Match[str]) -> str:
    coupon_amount = match_res.group(1)
    return '已新增優惠券, 價格: {amount}元, id: xTODO'.format(amount=coupon_amount)

supported_command=CouponBotMessageHandle(
    commands=[
        Command(r'/use (\w{5})', __handle_use),
        Command(r'/add (\w{5}) to (\w{3,})', __handle_add_to_user_id),
        Command(r'/add (\w{5})', __handle_add_to_all),
        Command(r'/create (\d+)', __handle_create_coupon),
    ]
)            
# supported_command=[re.compile(r'/use (\w{8})'), re.compile(r'/add (\d{1,8})'), re.compile(r'/add \d{8} to \w')]