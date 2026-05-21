import typer
from typing import Optional
from .client import BinanceFuturesClient
from .validators import validate_side, validate_order_type, validate_quantity, validate_price

# Initialize the Typer app
app = typer.Typer(help="Binance Futures Testnet Trading Bot CLI")

@app.command()
def trade(
    symbol: str = typer.Option(..., help="Trading pair symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., help="Order side: BUY or SELL"),
    order_type: str = typer.Option(..., help="Order type: MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Quantity to trade"),
    price: Optional[float] = typer.Option(None, help="Price (Required for LIMIT orders)")
):
    
    try:
        # Validate Inputs
        valid_side = validate_side(side)
        valid_type = validate_order_type(order_type)
        valid_quantity = validate_quantity(quantity)
        valid_price = validate_price(valid_type, price)

        # Print Request Summary 
        typer.secho("\n--- Order Request Summary ---", fg=typer.colors.CYAN, bold=True)
        typer.echo(f"Symbol:   {symbol.upper()}")
        typer.echo(f"Side:     {valid_side}")
        typer.echo(f"Type:     {valid_type}")
        typer.echo(f"Quantity: {valid_quantity}")
        if valid_type == "LIMIT":
            typer.echo(f"Price:    {valid_price}")
        typer.echo("-----------------------------\n")

        # Execute via Client
        client = BinanceFuturesClient()
        typer.echo("Sending request to Binance...")

        if valid_type == "MARKET":
            response = client.place_market_order(symbol.upper(), valid_side, valid_quantity)
        else:
            response = client.place_limit_order(symbol.upper(), valid_side, valid_quantity, valid_price)

        # Print Response Details
        typer.secho("\n✅ ORDER SUCCESSFUL", fg=typer.colors.GREEN, bold=True)
        typer.echo(f"Order ID:     {response.get('orderId')}")
        typer.echo(f"Status:       {response.get('status')}")
        typer.echo(f"Executed Qty: {response.get('executedQty')}")
        
        avg_price = response.get('avgPrice')
        if avg_price and float(avg_price) > 0:
            typer.echo(f"Avg Price:    {avg_price}")
        typer.echo("\n")

    except ValueError as ve:
        typer.secho(f"\n⚠️ VALIDATION ERROR: {ve}\n", fg=typer.colors.YELLOW, bold=True)
    except Exception as e:
        typer.secho(f"\n❌ EXECUTION FAILED: {str(e)}", fg=typer.colors.RED, bold=True)
        typer.echo("Check trading.log for full technical details.\n")

@app.command()
def cancel():
    """Placeholder for canceling orders later."""
    typer.echo("Cancel command coming soon.")

if __name__ == "__main__":
    app()