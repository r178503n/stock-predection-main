import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appDImageFallback]',
})
export class DImageFallbackDirective {
  @Input() imgFallback: string;
  constructor(private eRf: ElementRef) {
    //  console.log('___________________this is loading well_________________');
  }

  @HostListener('error')
  loadFallBackOnError() {
    //console.log(this.imgFallback);


    // console.log('___________________this is loading well_________________');
    const element: HTMLImageElement = <HTMLImageElement>this.eRf.nativeElement;
    element.src = this.imgFallback || 'static/images/noimage.jpg';
  }
}
