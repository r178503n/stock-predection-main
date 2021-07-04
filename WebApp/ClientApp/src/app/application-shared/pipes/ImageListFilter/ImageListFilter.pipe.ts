import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'ImageListFilter',
})
export class ImageListFilterPipe implements PipeTransform {
  transform(items: any, searchText: string): any[] {
    if (!items) {
      return [];
    }
    if (!searchText) {
      return items;
    }

    console.log(searchText);

    return items.filter((it) => {
      console.log();
      if (it['name'].toLowerCase().includes(searchText)) {
        return true;
      }
      return false;
    });
  }
}
