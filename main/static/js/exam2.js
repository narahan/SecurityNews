
if(!window['News']){
	News = {};

	(function (_O) {
		// console.log(_O)
		_O.start = function () {
			//scrollbar 
			$(function(){
				$('.t_body').mCustomScrollbar({
					theme: 'minimal-dark'
				});

			})
			_O.Event.set();

			// _O.Ctrl.set();
			// _O.Html.set();
			// _O.Data.set();
		};
		_O.Ajax = function(type){
			console.log('ooo::::', type)
		}
		_O.Vars = {
			flag: 1
		};
		_O.Ctrl = {
			set: function(){

			},
			slide_start: function(o){
				_O.Vars.start = setInterval(function() {
					_O.Ctrl.click(o);
				}, 3000);
			},
			click: function(o){
				var cl = o.attr('class');
				var slide_obj = $('.slide');
				var photo_obj = $('.photo');
				var time = 500;
				if(cl == 'prev_btn'){
					if(_O.Vars.point == 0){
						_O.Vars.point = 1;
						slide_obj.css('left', '-260px');
						slide_obj.prepend($('.photo:last-child'), slide_obj);//마지막 오브젝트를 처음으로 이동
					}
					_O.Vars.point--;
					slide_obj.stop().animate({
						left: '0'
					},time);
				}else {
					if(_O.Vars.point == 1){
						_O.Vars.point = 0;
						slide_obj.css('left','0');
						slide_obj.append($('.photo:first-child'), slide_obj);//처음 오브젝트 마지막으로 이동
					}
					_O.Vars.point++;
					slide_obj.stop().animate({
						left: '-260'
					},time);
				}
			}
		};
		_O.Event = {
			/**
			 * @author nara
			 * @brief 이벤트를 set한다.
			 */
			set: function(){
				var o;
				o = $('#wrap .tab');
				this.setObjAddEvent(o);
			},
			/**
			 * @author nara
			 * @brief 여러 오브젝트이면 루프로 이벤트 set, 아니면 단일 오브젝트 이벤트 set
			 * @param {object} o 오브젝트
			 */
			setObjAddEvent: function(o){
				// console.log('object:::', o);
				var length = o.length;
				if(length > 1){
					for(var i=0; i<length; i++){
						this.addEvent($(o[i]));
					}
				}else{
					if(length) this.add_event(o);
				}
			},
			/**
			 * @author nara
			 * @brief 이벤트 중복 방지하기위한 attribute set
			 * @param {object} o 오브젝트
			 * @return true or false
			 */
			checkBasicEvent: function (o) {
				if(!o.length) return false;
				if(o.attr('jBasicEvent')=='set') return true;
				else return false;
			},
			/**
			 * @author nara
			 * @brief 이벤트 실질적으로 넣는 함수.
			 * @param {object} o: 오브젝트, {object} event_category: 이벤트종류 및 콜백 오브젝트 ex)eventCategory = {'click':callback, ...}
			 */
			onEventAdd:function(o, event_category){
				$.each(event_category, function(index, item) {
					o.on(index, item);
				});
			},
			/**
			 * @author nara
			 * @brief 오브젝트에 따른 set하는 이벤트 분류
			 * @param {object} o: 오브젝트
			 */
			addEvent: function (o) {
				if(this.checkBasicEvent(o)) return;
				if(!o.length) { alert("Nara: setevent erro - no object", o); return; }
				$(o).attr('jBasicEvent','set');
				this.onEventAdd(o, {
					'click': function(e){
						e = e || window.event;//fireFox issue
						News.Event.onClick(o, e);
					}
				});
			},
			/**
			 * @author nara
			 * @brief 마우스 클릭 했을때 발생하는 이벤트
			 * @param {object} o: 오브젝트, {object} e:이벤트
			 */
			onClick: function(o, e){
				// console.log('On Click!!!', o)
				e = e || window.event;
				if(e.stopPropagation){
					e.stopPropagation();
				}else{
					e.returnValue = false;
					e.cancelBubble = true;
				}
				if(o.hasClass('tab')){
					var type, sel;
					type = o.attr('type');
					sel = o.attr('sel');
					
					// 클릭한 탭이 현재 열려있는 탭일때
					if(sel == 'on') {
						// console.log('true');
					}else{
						$('.tab[sel="on"]').attr('sel', 'off');
					
						if(sel == 'on'){
							o.attr('sel', 'off');
						}else{
							o.attr('sel', 'on');	
						}	
					}
					_O.Ajax(type);

					
				}
			}
		};
		_O.Data = {
			set: function(){
			}
		};
/// End.
	})(News);
}