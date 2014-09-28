import sys
import json
import combinations as combinations
import check_combinations as check_combinations

def main():
	result_set={}
	zappos={}
	check_list=[]
	price_list=[]
	zappos_file=open("output.txt")
	for zappos_line in zappos_file:
	#	print type(zappos_line)
		zappos = json.loads(zappos_line)
	#	print type(zappos)
	#	print zappos.encode('utf-8')
	result_set = zappos['results']
	for result in result_set:
		color_id = result['colorId']
		product_id = result['productId']
		product_name = result['productName']
		price = result['price'].encode('utf-8').replace('$','')
		check_list.append("Product ID:"+product_id+"#"+"Color ID:"+color_id+"#"+"Price:"+"$"+price)
		price_list.append(price)
		price_list=[int(float(i)) for i in price_list]
	#	print "color id"+str(color_id)
	#	print "price"+str(price)
	#	print "product id"+str(product_id)
	#	print "productName"+str(product_name)
#	print price_list
#	print json.dumps(check_list)
#	print type(check_list.values()[0])
#	print "going to call the function"
#	combinations.subset_sum(wanted_amount, price_list, total_price)
#	print check_list
	check_combinations.subset_sum(int(wanted_amount), check_list, int(float(total_price)))


if __name__ == '__main__':
	if len(sys.argv) > 2:
	#	print str(sys.argv[1])
		wanted_amount=sys.argv[1]
		total_price=sys.argv[2]
		main()
